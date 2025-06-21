import os

from rembg import remove
from PIL import Image
import io

if __name__ == '__main__':
    print("Running...")
    BASEDIR = "/home/claudia/PyCharmProjects/Photo_Processing"
    output_folder = os.path.join(BASEDIR, "removed_background")
    os.makedirs(output_folder, exist_ok=True)

    images_path = os.path.join(BASEDIR, 'to_remove_background')

    for image in os.listdir(images_path):
        filename = os.path.splitext(image)[0]
        image_path = os.path.join(images_path, image)

        # Load the image
        with open(image_path, 'rb') as f:
            input_image = f.read()

        # Remove background
        output_image = remove(input_image)

        # Load output into PIL Image
        image = Image.open(io.BytesIO(output_image))

        # Save as .webp
        image.save(os.path.join(output_folder, f'{filename}.webp'), "WEBP")

    print("Done")