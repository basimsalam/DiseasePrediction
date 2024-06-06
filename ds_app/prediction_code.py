import os
import cv2
from keras.engine.saving import load_model
import numpy as np
folders=os.listdir(r"C:\Users\HP\Desktop\archive\IMG_CLASSES")


y=[]
i=0
def readimg(fn):
    x = []
    image = cv2.imread(fn)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image= cv2.resize(gray_image, (48,48))
    x.append(gray_image)

    x = np.array(x, 'float32')


    x /= 255  # normalize inputs between [0, 1]


    x = x.reshape(x.shape[0], 48, 48, 1)

    return x



def predictfn(x):
    model=load_model(r"C:\Users\HP\PycharmProjects\ds\ds_app\model1.h5")

    f = readimg(x)
    folders = os.listdir(r"C:\Users\HP\Desktop\archive\IMG_CLASSES")
    r=model.predict_classes(f,verbose=0)
    return folders[r[0]]

# f=readimg("ISIC_0063740.jpg")
# r=predictfn(f)
#
# print(folders[r])