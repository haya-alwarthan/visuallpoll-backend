import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
# %matplotlib inline
DATA_PATH = './train-with-gps.csv'
IMG_ROOT = 'images'
# Read Data
data = pd.read_csv(DATA_PATH, delimiter=',')



# Get image as numpy array
def load_image(name, path):
    img_path = os.path.join(IMG_ROOT,name)
    img = cv2.imread(img_path)
    return img

# Plot numpy array
def plot_image(img):
    plt.imshow(img)
    plt.title(img.shape)
    plt.show()
    
# Plot a grid of examples
def plot_grid(img_names, img_root, rows=5, cols=5):
    fig = plt.figure(figsize=(25,25))
    
    for i,name in enumerate(img_names):
        fig.add_subplot(rows,cols,i+1)
        img = load_image(name, img_root)
        plot_image(img)
        
    plt.show()


#Try to plot 25 images
# plot_grid(data['image_path'][:25], IMG_ROOT)

def class_to_color(class_id):
    colors = [(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255),(255,100,100),
              (100,255,100),(100,100,255),(255,100,0),(255,0,100)]
    return colors[class_id]

# draw a single bounding box onto a numpy array image
def draw_bounding_box(img, annotation):
    if annotation.isnull().values.any():
        return
    
    x_min, y_min = int(annotation['xmin']), int(annotation['ymin'])
    x_max, y_max = int(annotation['xmax']), int(annotation['ymax'])
    
    class_id = int(annotation['class_id'])
    color = class_to_color(class_id)
    
    cv2.rectangle(img,(x_min,y_min),(x_max,y_max), color, 2)

# draw all annotation bounding boxes on an image
def annotate_image(img, name, all_annotations):
    annotations = all_annotations[all_annotations['image_path'] == name]
    for index, row in annotations.iterrows():
        draw_bounding_box(img, row)

def annotate_all():
    SAVE_PATH='annotated_images'
    for index, row in data.iterrows():
        img= load_image(row['image_path'],IMG_ROOT)
        draw_bounding_box(img,row)
        if not cv2.imwrite(os.path.join(SAVE_PATH,row['image_path']),img):
            raise Exception("Could not write file {} in the direcory".format(row['image_path']))



annotate_all()
# Plot a single sample with all its bounding boxes
# name = data.iloc[1002,1]
# img = load_image(name, IMG_ROOT)
# annotat
# _image(img, name, data)
# plot_image(img)
# if not cv2.imwrite(os.path.join('annotated_images',name),img):
#     raise Exception("could not write")
# cv2.waitKey(0)
