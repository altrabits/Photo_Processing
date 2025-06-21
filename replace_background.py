import os

import cv2
import numpy as np

def replace_using_rgb(image, rgb_color):
    # Load image
    image = cv2.imread(image)

    # Convert to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Define the white color range
    lower_white = np.array([230, 230, 230]) # adjust to capture the background
    upper_white = np.array([255, 255, 255])

    # Create a mask where white is detected
    mask = cv2.inRange(image_rgb, lower_white, upper_white)

    # Create color background (it must be in RGB)
    rgb_color = rgb_color

    # Create a background with the same shape as image
    colored_bg = np.full_like(image_rgb, rgb_color)

    # Replace white areas in image with new color
    result = np.where(mask[:, :, None] == 255, colored_bg, image_rgb)

    # Convert back to BGR and save or display
    result_bgr = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)

    return result_bgr

if __name__ == '__main__':
    print("Running...")
    BASEDIR = "/home/claudia/PyCharmProjects/Photo_Processing"
    output_folder = os.path.join(BASEDIR, "replaced_background")
    os.makedirs(output_folder, exist_ok=True)

    images_path = os.path.join(BASEDIR, 'to_remove_background')
    image = "Nano_Ethernet_side4_view-w-Broadcaster_Nano_Ethernet-IMG_1619.jpg"

    rgb_color = [238, 181, 67] # orange
    result_bgr_rgb = replace_using_rgb(os.path.join(images_path, image), rgb_color)
    cv2.imwrite(os.path.join(output_folder, f"output_{rgb_color}.jpg"), result_bgr_rgb)

    print("Done")
