import glob


def crawler(directory: str) -> list:
    return glob.glob(f"{directory}\\*.png")
