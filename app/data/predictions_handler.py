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
#try:
#model = tf.keras.models.load_model('trained_model_mobilenet.h5')
#except:
#    converter = tf.lite.TFLiteConverter.from_saved_model('trained_model_mobilenet.h5')
#    model = converter.convert()

def scale_range(input, min, max):
    input += -(np.min(input))
    input /= np.max(input) / (max - min)
    input += min
    return input

def get_prediction(model_input):

    img= cv2.imread(model_input)
    image_x = 300
    image_y = 300
    img = cv2.resize(img, (image_x, image_y))
    img = np.array(img, dtype=np.float32)
    img = np.reshape(img,  (image_x, image_y, 3))
    img = scale_range(img,-1,1)
    img = np.reshape(img,  (1, image_x, image_y, 3))

    pred_probab = model.predict(img)[0]
    pred_class = list(pred_probab).index(max(pred_probab))
    return labels[pred_class]

if __name__ == "__main__":
    test_input = input("is this a test? y/n ")
    if str(test_input) == "y":
        img_dir = "data/test_imgs/cardboard1.jpg"
        prediction = get_prediction(img_dir)
        print(prediction)
        #with os.scandir('data/test_imgs') as images:
            #for image in os.listdir(images):
                #temp = os.path.join(images, image)
                #print(temp)
                #image_pil = Image.open(f"data/test_imgs/{image.name}")
                # 1. load up test_imgs directory swith images
                # 2. uncomment prediction lines below once everything is set up to test
                # --->
                #prediction = get_prediction(temp)
                #print(prediction)
    print("done")
