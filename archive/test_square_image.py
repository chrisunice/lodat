import os
import cv2
import glob
import matplotlib.pyplot as plt

import lodat as lo


def test_square_image(test_assets_path, save_path):
    image_dir = f"{test_assets_path}\\images\\web"
    image_paths = glob.glob(f"{image_dir}\\*.png") + glob.glob(f"{image_dir}\\*.jpg")

    for path in image_paths:
        fig, ax = plt.subplots()
        image = cv2.imread(path)
        new_image = lo.utils.square_image(image, (810, 810))

        ax.imshow(cv2.cvtColor(new_image.numpy(), cv2.COLOR_BGR2RGB))
        fig.savefig(f"{save_path}\\{os.path.basename(path)}")
    assert len(os.listdir(save_path)) == len(image_paths)
