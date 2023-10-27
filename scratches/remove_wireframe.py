import cv2
import numpy as np
import matplotlib.pyplot as plt


def plot(image):
    fig, ax = plt.subplots()
    ax.imshow(image)
    fig.show()


if __name__ == '__main__':

    # Load the image
    img = cv2.imread(r"C:\LODAT\test_assets\xvv-311m000-f35a.X.baseupper.dat-003916-bwl2a.png")
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Show the original image
    # plot(img_rgb)

    # Set all white pixels to black
    lower_white = np.array([255, 255, 255])
    upper_white = np.array([255, 255, 255])

    white_mask = cv2.inRange(img_rgb, lower_white, upper_white)

    black = np.array([0, 0, 0], dtype=np.uint8)
    img_no_wf = img_rgb.copy()
    img_no_wf[white_mask > 0] = black

    # plot(img_no_wf)

    # Using OpenCV inpaint method to fill
    radius = 1
    method = cv2.INPAINT_TELEA
    inpainted_img = cv2.inpaint(img_rgb, white_mask, inpaintRadius=radius, flags=method)
    # plot(inpainted_img)

    # fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)
    # fig.suptitle(f'Radius = {radius} Method = {method}')
    # ax1.imshow(img_rgb)
    # ax2.imshow(inpainted_img)
    # fig.show()

    fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)
    fig.suptitle(f'Radius = {radius} Method = {method}')
    ax1.imshow(cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY), cmap='viridis')
    ax2.imshow(cv2.cvtColor(inpainted_img, cv2.COLOR_RGB2GRAY), cmap='viridis')
    fig.show()
