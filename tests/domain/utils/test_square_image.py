import glob
import matplotlib.pyplot as plt

import lodat as lo


def test_square_image(test_assets_path):
    image_paths = glob.glob(f"{test_assets_path}\\images\\web\\*.png")

    for path in image_paths:
        pass
