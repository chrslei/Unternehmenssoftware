import os
from PIL import Image

# function to convert image to grayscale
def convert_to_grayscale(image):
    return image.convert("L")

# specify the folder containing the images
folder_path = "train"

# loop through all files in the folder and its subfolders
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # check if the file is an image
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            # create the full path to the image
            image_path = os.path.join(root, file)

            # open the image
            image = Image.open(image_path)

            # convert the image to grayscale
            grayscale_image = convert_to_grayscale(image)

            # save the grayscale image
            grayscale_image.save(image_path)
