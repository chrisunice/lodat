"""
# Get extrema coordinates
top right (quadrant 1)
q1 = coords[(coords.x > centroid.x) & (coords.y > centroid.y)]
q1['distance'] = distance((q1.x, q1.y), centroid)
top_right = q1.iloc[q1.distance.argmax()][['x', 'y']].values

# top left (quadrant 2)
q2 = coords[(coords.x < centroid.x) & (coords.y > centroid.y)]
q2['distance'] = distance((q2.x, q2.y), centroid)
top_left = q2.iloc[q2.distance.argmax()][['x', 'y']].values

# bottom left (quadrant 3)
q3 = coords[(coords.x < centroid.x) & (coords.y < centroid.y)]
q3['distance'] = distance((q3.x, q3.y), centroid)
bottom_left = q3.iloc[q3.distance.argmax()][['x', 'y']].values

# bottom right (quadrant 4)
q4 = coords[(coords.x > centroid.x) & (coords.y < centroid.y)]
q4['distance'] = distance((q4.x, q4.y), centroid)
bottom_right = q4.iloc[q4.distance.argmax()][['x', 'y']].values
"""
import os
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def mod_img(cv2_image: np.ndarray):
    if cv2_image.ndim == 2:
        code = cv2.COLOR_GRAY2RGB
    else:
        code = cv2.COLOR_BGR2RGB
    return cv2.cvtColor(cv2_image, code)


def distance(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)


def is_rectangle(corners: np.ndarray, tolerance: int = 10):
    """
    Determines if the polygon is a quadrilateral
    :param corners: 4 x 2 array representing the corners of the polygon
    :param tolerance: the allowable difference in pixels for the two diagonals
    """
    top_left, bottom_left, bottom_right, top_right = corners
    diag1 = distance(top_left, bottom_right)
    diag2 = distance(top_right, bottom_left)
    if abs(diag1 - diag2) < tolerance:
        return True
    else:
        return False


def get_corners(coordinates: np.ndarray) -> np.ndarray:
    num_pts = len(coordinates)
    if num_pts == 4:
        # quadrilateral
        return coordinates
    elif num_pts > 4:
        # polygon
        coords = pd.DataFrame(data=coordinates, columns=['x', 'y'])

        # Get centroid
        width = coords.x.max() - coords.x.min()
        height = coords.y.max() - coords.y.min()
        centroid = pd.Series(data=dict(x=coords.x.min() + width/2, y=coords.y.min() + height/2))

        # Get corners
        top_left = centroid.x - width/2, centroid.y - height/2
        bottom_left = centroid.x - width/2, centroid.y + height/2
        bottom_right = centroid.x + width/2, centroid.y + height/2
        top_right = centroid.x + width/2, centroid.y - height/2

        return np.array([top_left, bottom_left, bottom_right, top_right], dtype='int')
    else:
        # Triangle or less
        raise ValueError(f'Not enough coordinates given. Received shape {coordinates.shape}')


if __name__ == '__main__':
    image_dir = r"C:\LODAT\test_assets\images"

    fig, ax = plt.subplots(nrows=5, ncols=len(os.listdir(image_dir)))

    for idx, fname in enumerate(os.listdir(image_dir)):
        # Original image
        img = cv2.imread(os.path.join(image_dir, fname))
        ax[0, idx].imshow(mod_img(img))
        if idx == 0:
            ax[0, idx].set_ylabel('Original')
        ax[0, idx].set_xticks([])
        ax[0, idx].set_yticks([])

        # Grayscale image
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ax[1, idx].imshow(mod_img(gray_img))
        if idx == 0:
            ax[1, idx].set_ylabel('Grayscale')
        ax[1, idx].set_xticks([])
        ax[1, idx].set_yticks([])

        # Thresholded image
        _, threshold_img = cv2.threshold(gray_img, 16, 255, cv2.THRESH_BINARY_INV)
        ax[2, idx].imshow(mod_img(threshold_img))
        if idx == 0:
            ax[2, idx].set_ylabel('Thresholded')
        ax[2, idx].set_xticks([])
        ax[2, idx].set_yticks([])

        # Get the contours
        contours, _ = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Get the biggest contour
        largest_contour = max(contours, key=cv2.contourArea)

        final_img = img.copy()
        cv2.drawContours(final_img, [largest_contour], -1, (0, 0, 255), 10)
        ax[3, idx].imshow(mod_img(final_img))
        if idx == 0:
            ax[3, idx].set_ylabel('Contour')
        ax[3, idx].set_xticks([])
        ax[3, idx].set_yticks([])

        # Crop image
        coords = largest_contour.reshape(-1, 2)
        corners = get_corners(coords)

        if is_rectangle(corners):
            x1, y1 = corners[0]
            x2, y2 = corners[2]
            crop_img = img[y1:y2, x1:x2, :]
        else:
            crop_img = img.copy()

        ax[4, idx].imshow(mod_img(crop_img))
        if idx == 0:
            ax[4, idx].set_ylabel('Crop')
        ax[4, idx].set_xticks([])
        ax[4, idx].set_yticks([])

    plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05, wspace=0.01, hspace=0.2)
    fig.show()
