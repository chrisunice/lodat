import cv2
import numpy as np
import lodat as lo
import matplotlib.pyplot as plt


def plot(image):
    fig, ax = plt.subplots()
    ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    fig.show()


if __name__ == '__main__':

    # Load the image
    img = cv2.imread(r"C:\LODAT\test_assets\xvv-311m000-f35a.X.baseupper.dat-003916-bwl2a.png")

    # Show the original image
    plot(img)

    # Show the wireframeless image
    new_image, wireframe = lo.utils.extract_wireframe(img)
    plot(new_image)

    # Show the wireframe
    fig, ax = plt.subplots()
    ax.scatter(wireframe[:, 0], wireframe[:, 1])
    ax.invert_yaxis()
    fig.show()

    # fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)
    # fig.suptitle(f'Radius = {radius} Method = {method}')
    # ax1.imshow(cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY), cmap='viridis')
    # ax2.imshow(cv2.cvtColor(inpainted_img, cv2.COLOR_RGB2GRAY), cmap='viridis')
    # fig.show()
