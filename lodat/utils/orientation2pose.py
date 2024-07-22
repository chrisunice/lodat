import numpy as np
import pymap3d as pm


def orientation2pose(
        target_position: tuple,
        target_attitude: tuple,
        observer_position: tuple,
        observer_attitude: tuple
) -> tuple:
    """

    :param target_position:
        lat, lon in degrees
        alt in meters
    :param target_attitude:
    :param observer_position:
    :param observer_attitude:
    :return:
    """

    if np.ndim(target_position) == 1:
        target_position = np.reshape(target_position, (-1, 1))

    # Convert coordinates to ENU frame relative to the observers location
    az, el, slant_range = pm.geodetic2aer(
        lat=target_position[0],
        lon=target_position[1],
        h=target_position[2],
        lat0=observer_position[0],
        lon0=observer_position[1],
        h0=observer_position[2],
        deg=True
    )

    # Convert azimuth and elevation to rotation matrices
    az = np.radians(az)
    az = az.reshape(-1, 1)
    r_az = np.zeros((len(az), 3, 3))
    r_az[:, 0, 0] = np.cos(az)[:, 0]
    r_az[:, 0, 1] = -1*np.sin(az)[:, 0]
    r_az[:, 1, 0] = np.sin(az)[:, 0]
    r_az[:, 1, 1] = np.cos(az)[:, 0]
    r_az[:, 2, 2] = 1

    el = np.radians(el)
    el = el.reshape(-1, 1)
    r_el = np.zeros((len(el), 3, 3))
    r_el[:, 0, 0] = np.cos(el)[:, 0]
    r_el[:, 0, 2] = np.sin(el)[:, 0]
    r_el[:, 1, 1] = 1
    r_el[:, 2, 0] = -1*np.sin(el)[:, 0]
    r_el[:, 2, 2] = np.cos(el)[:, 0]

    # Convert target(s) and observer attitude to rotation matrices
    r_target = _rotation_matrix(
        roll=target_attitude[0],
        pitch=target_attitude[1],
        yaw=target_attitude[2],
        is_target=True,
        degrees=True
    )
    r_observer = _rotation_matrix(
        roll=observer_attitude[0],
        pitch=observer_attitude[1],
        yaw=observer_attitude[2],
        is_target=False,
        degrees=True
    )

    # Composite rotation matrix
    rmat = r_target @ r_observer @ r_az @ r_el

    # Calculate look, depression, twist
    look = np.arctan2(-1 * rmat[:, 1, 0], -1 * rmat[:, 0, 0])
    look = np.mod(np.round(np.degrees(look), 6), 360)

    depression = np.arcsin(rmat[:, 2, 0])
    depression = np.degrees(depression)

    twist = np.arctan2(-1 * rmat[:, 2, 1], rmat[:, 2, 2])
    twist = np.degrees(twist)

    pose = np.array([look, depression, twist, slant_range])

    return pose.squeeze()


def _rotation_matrix(
        roll: int | float | np.ndarray,
        pitch: int | float | np.ndarray,
        yaw: int | float | np.ndarray,
        is_target: bool = True,
        degrees: bool = True
):
    """
    Calculates the composite rotation matrix

    :param roll: aircraft roll angle in degrees
    :param pitch: aircraft pitch angle in degrees
    :param yaw: aircraft yaw (heading) angle in degrees
    :param is_target: True for rotation from target perspective; False from observer perspective
    :param degrees: True if `roll`, `pitch`, `yaw` are given in degrees; False for radians

    :return: rotation matrix
    """
    if degrees:
        # Attitude in radians
        roll = np.radians(roll)
        pitch = np.radians(pitch)
        yaw = np.radians(yaw)

    # Sign factor for target or observer
    if is_target:
        k, j = (-1, 1)
    else:
        k, j = (1, -1)

    # Component matrices
    roll = np.reshape(roll, (-1, 1))
    r_roll = np.zeros((len(roll), 3, 3))
    r_roll[:, 0, 0] = 1
    r_roll[:, 1, 1] = np.cos(roll)[:, 0]
    r_roll[:, 1, 2] = j * np.sin(roll)[:, 0]
    r_roll[:, 2, 1] = k * np.sin(roll)[:, 0]
    r_roll[:, 2, 2] = np.cos(roll)[:, 0]

    pitch = np.reshape(pitch, (-1, 1))
    r_pitch = np.zeros((len(pitch), 3, 3))
    r_pitch[:, 0, 0] = np.cos(pitch)[:, 0]
    r_pitch[:, 0, 2] = k * np.sin(pitch)[:, 0]
    r_pitch[:, 1, 1] = 1
    r_pitch[:, 2, 0] = j * np.sin(pitch)[:, 0]
    r_pitch[:, 2, 2] = np.cos(pitch)[:, 0]

    yaw = np.reshape(yaw, (-1, 1))
    r_yaw = np.zeros((len(yaw), 3, 3))
    r_yaw[:, 0, 0] = np.cos(yaw)[:, 0]
    r_yaw[:, 0, 1] = j * np.sin(yaw)[:, 0]
    r_yaw[:, 1, 0] = k * np.sin(yaw)[:, 0]
    r_yaw[:, 1, 1] = np.cos(yaw)[:, 0]
    r_yaw[:, 2, 2] = 1

    # Composite matrix
    if is_target:
        rotation_matrix = r_roll @ r_pitch @ r_yaw
    else:
        rotation_matrix = r_yaw @ r_pitch @ r_roll
    return rotation_matrix
