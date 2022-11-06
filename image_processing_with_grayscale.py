import sys
import cv2
import os
sys.path.append('/usr/local/lib/python3.9/site-packages')
# function to opden all images from a folder and resize them all to a size of 500px x 500px, make them into greyscale and save them in a new folder
original_images = os.listdir('original_images')
for image in original_images:
    img = cv2.imread('original_images/' + image)
    img = cv2.resize(img, (500, 500))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('resized_images/' + image, img)
