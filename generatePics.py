import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import time
import tensorflow as tf
print(tf.__version__)
import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt

def generate_pic(username):

    # https://github.com/keras-team/keras-io/issues/1912

    model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)

    images = model.text_to_image(
        f"space nebula for name {username}",
        batch_size=1,
    )

    def plot_images(images):
        plt.figure(figsize=(20, 20))
        for i in range(len(images)):
            ax = plt.subplot(1, len(images), i + 1)
            plt.imshow(images[i])
            plt.axis("off")
            plt.show()

    plot_images(images)

