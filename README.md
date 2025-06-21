# Photo Processing

## AI-Based Background Removal Library
AltraBits uses **rembg** to perform fast and local AI-based background removal from photos.

Rembg uses **U-2-Net**, a deep learning model for salient object detection.
It is **free and fast and works offline**.

Quick start example:

```
from rembg import remove
from PIL import Image

input_path = 'input.jpg'
output_path = 'output.png'

input_image = Image.open(input_path)
output_image = remove(input_image)

output_image.save(output_path)
```


## Folder-Based Photo Processing

Use the script `remove_background.py` to process all **.jpg** images in the `to_remove_background` folder.

### Preparing images from CR2 format
Before using the script, prepare your images as follows:
- **Open the CR2 photo** on Windows using the default Photo viewer
- Use the **Edit** tool to:
  - Crop to a square format
  - Center the object
  - Rotate if necessary
  - Appy Auto Enhance and manually adjust settings if needed
- Save the edited image using the following naming format `product_name-w-tags_go_here-IMG-0000.jpg`

### Running the removal tool
After placing the edited images in the `to_remove_background`, run the script. 
The processed images with the background removed will be saved in the `removed_background` folder.
The processed images now have the extension **webp**.

> **Note**: This script uses **rembg** with **onnxruntime** for background removal.
