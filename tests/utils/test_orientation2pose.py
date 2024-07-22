import pytest
import numpy as np
from lodat.utils.orientation2pose import orientation2pose


@pytest.fixture()
def observer_position():
    lat = 36.7341597
    lon = -117.2166654
    alt = 11000 * 0.3048
    return lat, lon, alt


@pytest.fixture()
def observer_attitude():
    roll = 0
    pitch = 0
    heading = 0
    return roll, pitch, heading


def test_single_inputs(observer_position, observer_attitude):
    target_lat = 36.7290516
    target_lon = -117.2165206
    target_alt = 11500 * 0.3048
    target_roll = 0
    target_pitch = 4
    target_heading = 355

    look, depr, twist, srange = orientation2pose(
        target_position=(target_lat, target_lon, target_alt),
        target_attitude=(target_roll, target_pitch, target_heading),
        observer_position=observer_position,
        observer_attitude=observer_attitude
    )

    rounded_pose = np.round((look, depr, twist), 0)
    answers = np.array([4, -19, 0])

    assert np.alltrue(rounded_pose == answers)


def test_multiple_inputs(observer_position, observer_attitude):
    target_lat = [36.7290516, 36.7290516]
    target_lon = [-117.2165206, -117.2165206]
    target_alt = [11500 * 0.3048, 11500 * 0.3048]
    target_roll = [0, 0]
    target_pitch = [4, 4]
    target_heading = [355, 355]

    look, depr, twist, srange = orientation2pose(
        target_position=(target_lat, target_lon, target_alt),
        target_attitude=(target_roll, target_pitch, target_heading),
        observer_position=observer_position,
        observer_attitude=observer_attitude
    )

    rounded_pose = np.round((look, depr, twist), 0)
    answers = np.array([4, -19, 0]).reshape(-1, 1)

    assert np.alltrue(rounded_pose == answers)