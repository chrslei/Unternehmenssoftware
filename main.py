import os
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tf as tf
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
from PIL import Image
from glob import glob
# from google.colab import drive
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import load_img, img_to_array

'''
train_data = pd.read_csv("UTSoftware/train.csv")
train_paths = train_data["path"].unique()
print(train_paths)

validate_data = pd.read_csv("UTSoftware/validate.csv")
validate_path = validate_data["path"].unique()
print(validate_path)


# Displaying the image
img = tf.keras.utils.load_img("UTSoftware/Dataset_1/low-resolution/200-n000008-Airedale/n107026.jpg",
                              target_size=(100, 100))
plt.imshow(img)
plt.axis("off")
plt.show()

# Printing the shape of the image array
x = tf.keras.utils.img_to_array(img)
print(x.shape)
'''

# Setting Training, Validate & Test dir paths
train_path = 'train/'
validate_path = "validate/"
test_path = 'test/'

# Finding number of classes
className = glob(train_path + '/*')
number_of_class = len(className)
print(number_of_class)

img = load_img(train_path + "affenpinscher/n107845.jpg", target_size=(100, 100))
x = img_to_array(img)

# Creating the model
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=x.shape))
model.add(Activation("relu"))
model.add(MaxPooling2D())
model.add(Conv2D(32, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D())
model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(1024))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(number_of_class))
model.add(Activation("softmax"))

# Compiling the model
model.compile(loss="categorical_crossentropy", optimizer="rmsprop", metrics=["accuracy"])

# Getting model's summary
model.summary()

# Specifing epochs & batch size
epochs = 100
batch_size = 64

# Creating an object of ImageDataGenerator.
train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.3,
                                   horizontal_flip=True,
                                   zoom_range=0.3)
validate_datagen = ImageDataGenerator(rescale=1./255)

# Generating batches of Augmented data.
train_generator = train_datagen.flow_from_directory(directory=train_path,
                                                    target_size=x.shape[:2],
                                                    batch_size=batch_size,
                                                    color_mode="rgb",
                                                    class_mode="categorical")

validate_generator = validate_datagen.flow_from_directory(directory=validate_path,
                                                          target_size=x.shape[:2],
                                                          batch_size=batch_size,
                                                          color_mode="rgb",
                                                          class_mode="categorical")

# Fitting the model
hist = model.fit_generator(generator=train_generator,
                           steps_per_epoch=1600 // batch_size,
                           epochs=epochs,
                           validation_data=validate_generator,
                           validation_steps=800 // batch_size)

# Plotting train & validation loss
plt.figure()

plt.plot(hist.history["loss"],
         label="Train Loss",
         color="black")

plt.plot(hist.history["val_loss"],
         label="Validation Loss",
         color="mediumvioletred",
         linestyle="dashed",
         markeredgecolor="purple",
         markeredgewidth=2)

plt.title("Model Loss",
          color="darkred",
          size=13)

plt.legend()
plt.show()

# Plotting train & validation accuracy
plt.figure()
plt.plot(hist.history["accuracy"],
         label="Train Accuracy",
         color="black")

plt.plot(hist.history["val_accuracy"],
         label="Validation Accuracy",
         color="mediumvioletred",
         linestyle="dashed",
         markeredgecolor="purple",
         markeredgewidth=2)

plt.title("Model Accuracy",
          color="darkred",
          size=13)

plt.legend()
plt.show()

# Taking a Single Image for Prediction
# Displaying the selected image
img = load_img(test_path + "golden_retriever/n155800.jpg", target_size=(100, 100))
plt.imshow(img)
plt.axis("off")
plt.show()


def load(filename):
    '''

    :param filename:
    :return:
    '''
    np_image = Image.open(filename)
    np_image = np.array(np_image).astype('float32')/255
    np_image = np.expand_dims(np_image, axis=0)
    return np_image


image = load(test_path + "golden_retriever/n155800.jpg")

# Predicting the class
prediction = (np.argmax(model.predict(image), axis=-1))
print(prediction)

# Printing class dictionary
print(validate_generator.class_indices)
