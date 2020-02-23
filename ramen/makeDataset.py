import matplotlib.pyplot as plt
import sys
from keras.preprocessing.image import array_to_img,img_to_array,load_img
import numpy as np
import os

# datasets import for mario dataset
X_train=[]
Y_train=[]

X_test=[]
Y_test=[]

data=os.listdir("./images")

for i in data:
	print(i)