import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def mod_img(cv2_image: np.ndarray):
    if cv2_image.ndim == 2:
        code = cv2.COLOR_GRAY2RGB
    else:
        code = cv2.COLOR_BGR2RGB
    return cv2.cvtColor(cv2_image, code)


if __name__ == '__main__':
    image_dir = r"C:\LODAT\test_assets\images"

    fig, ax = plt.subplots(nrows=4, ncols=4)

    for idx, fname in enumerate(os.listdir(image_dir)):
        # Original image
        img = cv2.imread(os.path.join(image_dir, fname))
        ax[idx, 0].imshow(mod_img(img))
        ax[idx, 0].set_title('Original')

        # Grayscale image
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ax[idx, 1].imshow(mod_img(gray_img))
        ax[idx, 1].set_title('Grayscale')

        # Thresholded image
        _, threshold_img = cv2.threshold(gray_img, 16, 255, cv2.THRESH_BINARY_INV)
        ax[idx, 2].imshow(mod_img(threshold_img))
        ax[idx, 2].set_title('Thresholded')

        # Get the contours
        contours, _ = cv2.findContours(threshold_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Get the biggest contour
        largest_contour = max(contours, key=cv2.contourArea)

        final_img = img.copy()
        cv2.drawContours(final_img, [largest_contour], -1, (0, 0, 255), 10)
        ax[idx, 3].imshow(mod_img(final_img))
        ax[idx, 3].set_title('Final')

        # Bounding box points
        box = largest_contour.reshape(-1, 2)
        top_left, bottom_left, bottom_right, top_right = box

        print(f'\n{fname} Area of Interest:')
        print('Top left', top_left)
        print('Bottom left', bottom_left)
        print('Bottom right', bottom_right)
        print('Top right', top_right)

    fig.show()
