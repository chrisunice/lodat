import cv2
import numpy as np
import tensorflow as tf


def square_image(image: np.ndarray, dst_size: tuple[int, int]):
    """ TODO add desc """
    h, w, c = image.shape
    is_square = (h == w)
    if is_square:
        image = cv2.resize(image, dst_size)
    else:
        image = tf.image.resize_with_crop_or_pad(image, *dst_size)

    return image
