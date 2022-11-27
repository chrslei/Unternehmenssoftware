import os
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tf as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
#from keras_preprocessing.image import ImageDataGenerator, img_to_array, load_img
#from tensorflow.keras.utils import load_img
from PIL import Image
from glob import glob
# from google.colab import drive

train_data = pd.read_csv("UTSoftware/train.csv")
train_paths = train_data["path"].unique()
print(train_paths)

validate_data = pd.read_csv("UTSoftware/validate.csv")
validate_path = validate_data["path"].unique()
print(validate_path)

'''
# Displaying the image
img = tf.keras.utils.load_img("UTSoftware/Dataset_1/low-resolution/200-n000008-Airedale/n107026.jpg",
                              target_size=(100, 100))
plt.imshow(img)
plt.axis("off")
plt.show()

# Printing the shape of the image array
x = tf.keras.utils.img_to_array(img)
print(x.shape)



#Creating the model
model = Sequential()
model.add(Conv2D(32,(3,3),input_shape = x.shape))
model.add(Activation("relu"))
model.add(MaxPooling2D())model.add(Conv2D(32,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D())model.add(Conv2D(64,(3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D())model.add(Flatten())
model.add(Dense(1024))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(number_of_class))
model.add(Activation("softmax"))
#Compiling the model
model.compile(loss = "categorical_crossentropy",
optimizer = "rmsprop",
metrics = ["accuracy"])
#Getting model's summary
model.summary()
'''
