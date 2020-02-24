import tensorflow as tf
import cv2
import keras
import numpy as np
import sys

args = sys.argv

# モデルのロード
model = keras.models.load_model("saved_models/keras_mario_trained_model_resnet.h5")

image = cv2.imread(args[1])


image = cv2.resize(image, (64,64))
cv2.imshow('frame',image)
cv2.waitKey(1)
image = image.reshape((1,64,64,3))/255


result = model.predict(image)

print(result)

if np.argmax(result) == 0:
    print("mario")
    print("confidence:"+"{0:.3f}".format(result[0][0]))
else:
    print("nonmario")
    print("confidence:"+"{0:.3f}".format(result[0][1]))

cv2.destroyAllWindows()