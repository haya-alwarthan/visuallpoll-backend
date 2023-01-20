import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import sys
import torch
from PIL import Image
import pandas
def load_image(path):
    img = cv2.imread(path)
    return img

# Plot numpy array
def plot_image(img):
    plt.imshow(img)
    plt.title(img.shape)
    plt.show()


def draw_bounding_box(path):
    
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./yolov5train1.pt')
    print("after model load")
    img= load_image(path)
    # Inference
    results = model(img, size=640) # batch of images
    r_img = results.render() # returns a list with the images as np.array
    img = r_img[0] # image with boxes as np.array\
    return img

    