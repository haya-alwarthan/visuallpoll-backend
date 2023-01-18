import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import json 
# %matplotlib inline
DATA_PATH = './train-with-gps.csv'
IMG_ROOT = 'images'
# Read Data
data = pd.read_csv(DATA_PATH, delimiter=',')
dict={}
dataset_dict = {}
set

def dict_to_json(dic):
    portion= dic[:5]
    print(portion)
    f = open("demojson.json", "w")
    f.write(portion.to_json(orient='index'))
    f.close()


# def generate_dict():
#     for index,row in data.iterrows():
#         if row['image_path'] not in dict:
#             dict[row['image_path']]={'bboxes':[],'classes':[],'lat':0,'lon':0}
#             bbox={'xmin':row['xmin'],'xmax':row['xmax'],'ymin':row['ymin'],'ymax':row['ymax']}
#         dict[row['image_path']]['bboxes'].append(bbox)
#         dict[row['image_path']]['classes'].append(row['class_id'])
#         dict[row['image_path']]['lat']=row['lat']
#         dict[row['image_path']]['lon']=row['long']
#         print(dict)

def generate_dict():
    for index,row in data.iterrows():
        if row['image_path'] not in dict.keys():
            dict[row['image_path']]={'names':set(),'classes':set()}
        dict[row['image_path']]['names'].add(row['name'])
        dict[row['image_path']]['lat']=row['lat']
        dict[row['image_path']]['lon']=row['long']
        dict[row['image_path']]['classes'].add(row['class_id'])
        dict[row['image_path']]['image_path']=row['image_path']
        dict[row['image_path']]['title']=generateRandomTitle()


        
def dict_to_json():
    dict_index={}
    count=0
    for key,value in dict.items():
        value['names']= list(value['names'])
        value['classes']= list(value['classes'])
        dict_index[count]=value
        count=count+1
    json_object = json.dumps(dict_index, indent = 4) 
    dataset_dict=dict_index
    f = open("demojson.json", "w")
    if not f.write(json_object):
        raise Exception("did not write succefully")
    f.close()
    
def generateRandomTitle():
    ran =  random.randint(0,10)
    lis=['النسيم 19344','النسيم 47922','العليا 2344','هجر 28495','الضاحية 4789','1245 طريق الملك فهد','حي النعمان3945 ','9435 طريق الخليج','8458 شارع أبي بكر الصديق','طريق الملك عبدالله 4345','طريق عمر ابن الخطاب 2664']
    return lis[ran]
   


generate_dict()  
dict_to_json()

