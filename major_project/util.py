import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

model = None
labels = ['cardboard','glass','metal','paper','plastic','trash']

def load_artifacts():
    global model
    model = tf.keras.models.load_model("model_300.h5")

def classify_waste(img_path):
    global labels
    img = Image.open(img_path).show()
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(300,300))
    img = tf.keras.preprocessing.image.img_to_array(img, dtype=np.uint8)
    img = np.array(img)/255.0
    p=model.predict(img[np.newaxis, ...])
    print("Predicted shape",p.shape)
    print("Maximum Probability: ",np.max(p[0], axis=-1))
    # for x in p:
    #     print(x)
    predicted_class = labels[np.argmax(p[0], axis=-1)]
    print("Classified:",predicted_class)
    return str(predicted_class)