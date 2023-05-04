from PIL import Image
import os

# Set the directory containing the images
directory = "C:/Berkeley/spring2023/sdse/categorize_ethnicity/val_raw/Black"

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"): # Check if the file is an image
        # Open the image and convert it to grayscale
        filepath = os.path.join(directory, filename)
        with Image.open(filepath) as img:
            grayscale_img = img.convert('L')
            # Save the grayscale image
            grayscale_img.save(filepath)
