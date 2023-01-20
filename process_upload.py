import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import sys
def load_image(path):
    img = cv2.imread(path)
    return img

# Plot numpy array
def plot_image(img):
    plt.imshow(img)
    plt.title(img.shape)
    plt.show()


def draw_bounding_box(path):
    img= load_image(path)
    cv2.rectangle(img,(100,100),(250,250), (100,255,100), 2)
    return img

    