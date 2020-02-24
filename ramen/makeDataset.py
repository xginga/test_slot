import matplotlib.pyplot as plt
import sys
from keras.preprocessing.image import array_to_img,img_to_array,load_img
import numpy as np
import os
from sklearn.model_selection import train_test_split
from keras.utils import np_utils

# datasets import for mario dataset
X=[]
Y=[]

# 対象Aの画像
for picture in list_pictures('./images/datasets/0mario'):
    img = img_to_array(load_img(picture, target_size=(64,64)))
    X.append(img)

    Y.append(0)


# 対象Bの画像
for picture in list_pictures('./images/datasets/1nomario'):
    img = img_to_array(load_img(picture, target_size=(64,64)))
    X.append(img)

    Y.append(1)


X=np.asarray(X)
Y=np.asarray(Y)

X=X.astype('float32')
X=X/255.0

Y=np_utils.to_categorical(Y,2)

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=111)