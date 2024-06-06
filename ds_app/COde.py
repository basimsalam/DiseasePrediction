import os
import cv2


folders=os.listdir("D:\\PROJECT\\archive1\\IMG_CLASSES")
# print(folders)
x=[]
y=[]
i=0
for f in folders:
    # print(f)
    files=os.listdir(os.path.join("D:\\PROJECT\\archive1\\IMG_CLASSES",f))
    # print(files)
    print("===============================================================")
    for img in files:
        print(os.path.join("D:\\PROJECT\\archive1\\IMG_CLASSES",f,img))
        image = cv2.imread(os.path.join("D:\\PROJECT\\archive1\\IMG_CLASSES",f,img))
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_image= cv2.resize(gray_image, (48,48))
        x.append(gray_image)
        y.append(i)
    i=i+1

# coding: utf-8

# In[ ]:


import tensorflow as tf

import keras
from keras.engine.saving import load_model
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from keras.layers import Dense, Activation, Dropout, Flatten
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
num_classes =10
batch_size = 80
epochs = 300
#------------------------------
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.engine.saving import load_model
# manipulate with numpy,load with panda
import numpy as np
# import pandas as pd
x=np.asarray(x, dtype=np.float32)
y=np.asarray(y)
from sklearn.model_selection import train_test_split
# load dataset
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
y_train1=[]
for i in y_train:
    op = keras.utils.to_categorical(i, num_classes)

    y_train1.append(op)

y_train=y_train1

x_train = np.array(X_train, 'float32')
y_train = np.array(y_train, 'float32')
x_test = np.array(X_test, 'float32')
y_test = np.array(y_test, 'float32')
x_train /= 255  # normalize inputs between [0, 1]
x_test /= 255
print("x_train.shape",x_train.shape)
x_train = x_train.reshape(x_train.shape[0], 48, 48, 1)
x_train = x_train.astype('float32')
x_test = x_test.reshape(x_test.shape[0], 48, 48, 1)
x_test = x_test.astype('float32')
# construct CNN structure
model = Sequential()
# 1st convolution layer
model.add(Conv2D(64, (5, 5), activation='relu', input_shape=(48, 48, 1)))
model.add(MaxPooling2D(pool_size=(5, 5), strides=(2, 2)))
# 2nd convolution layer
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))
# 3rd convolution layer
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))
model.add(Flatten())
# fully connected neural networks
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))
# ------------------------------
# batch process
gen = ImageDataGenerator()
train_generator = gen.flow(x_train, y_train, batch_size=batch_size)

# ------------------------------

model.compile(loss='categorical_crossentropy'
              , optimizer=keras.optimizers.Adam()
              , metrics=['accuracy']
              )
# ------------------------------
if not os.path.exists("model1.h5"):

    model.fit_generator(train_generator, steps_per_epoch=batch_size, epochs=epochs)
    model.save("model1.h5")  # train for r+andomly selected one
else:
    model = load_model("model1.h5")  # load weights


from sklearn.metrics import confusion_matrix
yp=model.predict_classes(x_test,verbose=0)
cf=confusion_matrix(y_test,yp)
print(cf)
