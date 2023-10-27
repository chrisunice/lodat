import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def remove_background(image: np.ndarray) -> np.ndarray:
    # Define a threshold for white color (in BGR)
    lower_white = np.array([225, 225, 225])
    upper_white = np.array([255, 255, 255])

    # Create a mask for the white background
    mask = cv2.inRange(image, lower_white, upper_white)

    # Invert the mask
    mask = cv2.bitwise_not(mask)

    # Convert your image to RGBA (adding an alpha channel)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

    # Set the alpha channel using the mask
    image[:, :, 3] = mask

    return image


if __name__ == '__main__':

    path_to_image = r"C:\Users\ChrisUnice\Downloads\mtsi_logo.jpg"
    new_name = 'mtsi_logo_transparent.png'

    old_image = cv2.imread(path_to_image)
    new_image = remove_background(old_image)

    # Convert both images to RGB format (matplotlib uses RGB)
    original_image_rgb = cv2.cvtColor(old_image, cv2.COLOR_BGR2RGB)
    new_image_rgb = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)

    # Create a figure with two subplots (side by side)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    fig.patch.set_facecolor('black')  # Set the figure background to black

    # Display the original image on the left subplot
    ax1.set_title("Original Image")
    ax1.imshow(original_image_rgb)

    # Display the new image with a transparent background on the right subplot
    ax2.set_title("New Image with Transparent Background")
    ax2.imshow(new_image_rgb)

    # Hide axes and display the images
    ax1.axis('off')
    ax2.axis('off')

    # Show the images side by side
    plt.show()

    # Save image
    output_path = f"{os.path.dirname(path_to_image)}\\{new_name}"
    cv2.imwrite(output_path, new_image)