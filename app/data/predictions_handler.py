import os
from PIL import Image
import tensorflow as tf
import numpy as np
import cv2
import glob

labels = {0: 'cardboard', 1: 'glass',
          2: 'metal', 3: 'paper',
          4: 'patic', 5: 'trash'}

model = tf.keras.models.load_model("data/test2.h5")


def scale_range(input, min, max):
    input += -(np.min(input))
    input /= np.max(input) / (max - min)
    input += min
    return input


def get_prediction(model_input):
    nparr = np.fromstring(model_input, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    image_x = 300
    image_y = 300
    img = cv2.resize(img, (image_x, image_y))
    img = np.array(img, dtype=np.float32)
    img = np.reshape(img,  (image_x, image_y, 3))
    img = scale_range(img, -1, 1)
    img = np.reshape(img,  (1, image_x, image_y, 3))
    pred_probab = model.predict(img)[0]
    pred_class = list(pred_probab).index(max(pred_probab))
    return labels[pred_class]


if __name__ == "__main__":
    test_input = input("is this a test? y/n ")
    if str(test_input) == "y":
        with os.scandir('data/test_imgs') as images:
            for image in images:
                prediction = get_prediction(f"data/test_imgs/{image.name}")
                print(prediction)
