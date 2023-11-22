import cv2
import numpy as np


def extract_wireframe(image: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
    Separates the wireframe from the image and fills the data with the average of neighboring pixels

    :param image: image in BGR format
    :return:
        * new_image - image in BGR format without a wireframe
        * wireframe - x,y coordinates of the wireframe
    """
    # Assumes the wireframe is white
    lower_white = np.array([255, 255, 255])
    upper_white = np.array([255, 255, 255])

    # Create mask for white pixels
    white = cv2.inRange(image, lower_white, upper_white)
    white_mask = white > 0

    # Remove the wireframe from the image
    new_image = cv2.inpaint(image, white, inpaintRadius=1, flags=cv2.INPAINT_TELEA)

    # Get the wireframe
    wireframe = np.column_stack(np.where(white_mask))

    return new_image, wireframe
