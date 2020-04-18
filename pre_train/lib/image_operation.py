#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:17:35 2020

@author: haoqiwang
"""

import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import copy

from lib import csv_operation
from lib import pixel_operation


'''

show original image

Example:
    
from lib import image_operation

IMAGE_FOLDER='./image_database/'
image_name = 'natural_forest.jpg'

image_path=IMAGE_FOLDER+image_name

ori_image = image_operation.read_image(image_path)

'''

def read_image(image_path):
    ori_image = mpimg.imread(image_path)
    image = np.asarray(ori_image).astype(np.int32)
    plt.imshow(image)
    plt.xticks([])
    plt.yticks([])    
    return image

'''

remove one color

Example:
    
from lib import image_operation

IMAGE_FOLDER='./image_database/'
image_name = 'natural_forest.jpg'

image_path=IMAGE_FOLDER+image_name

#remove red
ori_image = image_operation.read_image(image_path)

image_remove_red=image_operation.remove_red(ori_image)

#remove green
ori_image = image_operation.read_image(image_path)

image_remove_green=image_operation.remove_green(ori_image)

#remove blue
ori_image = image_operation.read_image(image_path)

image_remove_blue=image_operation.remove_blue(ori_image)

'''


def remove_red(image):
    image_remove_red = copy.deepcopy(image)
    image_remove_red[:, :, 0] = 0
    plt.imshow(image_remove_red)
    plt.xticks([])
    plt.yticks([])
    return image_remove_red


def remove_green(image):
    image_remove_green = copy.deepcopy(image)
    image_remove_green[:, :, 1] = 0
    plt.imshow(image_remove_green)
    plt.xticks([])
    plt.yticks([])
    return image_remove_green


def remove_blue(image):
    image_remove_blue = copy.deepcopy(image)
    image_remove_blue[:, :, 2] = 0
    plt.imshow(image_remove_blue)
    plt.xticks([])
    plt.yticks([])
    return image_remove_blue

'''

remove color and recover color

Example:
    
from lib import image_operation

IMAGE_FOLDER='./image_database/'
image_name = 'natural_forest.jpg'

image_path=IMAGE_FOLDER+image_name

#remove and recover red
ori_image = image_operation.read_image(image_path)

image_remove_red=image_operation.remove_red(ori_image)

image_recover_red=image_operation.recover_red(image_remove_red)

#remove and recover green
ori_image = image_operation.read_image(image_path)

image_remove_green=image_operation.remove_green(ori_image)

image_recover_green=image_operation.recover_green(image_remove_green)

#remove and recover blue
ori_image = image_operation.read_image(image_path)

image_remove_blue=image_operation.remove_blue(ori_image)

image_recover_blue=image_operation.recover_blue(image_remove_blue)

'''
def recover_red(image_remove_red):
    RG_matrix, RG_record_matrix, RB_matrix, RB_record_matrix, GB_matrix, GB_record_matrix = csv_operation.import_csv()
    
    image_recover_red = copy.deepcopy(image_remove_red)
    
    image_size = image_remove_red.shape

    #num_channel = image_size[2]
    num_row = image_size[0]  # how many rows
    num_column = image_size[1]  # how many columns
    
    #initialize recoverd_red to store
    recovered_red=np.zeros((num_row,num_column),dtype=np.int32)
    #for now, we recover the image except edge
    for i in np.arange(1, num_row - 1):
        for j in np.arange(1, num_column - 1):
            green_value = image_remove_red[i, j, 1]
            blue_value = image_remove_red[i, j, 2]

            green_contrast = pixel_operation.rms_contrast(image_remove_red, i, j, 1)
            blue_contrast = pixel_operation.rms_contrast(image_remove_red, i, j, 2)

            green_blue_contrast_mean = (green_contrast + blue_contrast) / 2
            
            GB_matrix_index = pixel_operation.contrast_index(green_blue_contrast_mean)
            
            recovered_red[i,j]=GB_matrix[blue_value,green_value,GB_matrix_index]
    
    image_recover_red[:,:,0]=recovered_red

    plt.imshow(image_recover_red)
    plt.xticks([])
    plt.yticks([])
    
    return image_recover_red


def recover_green(image_remove_green):
    RG_matrix, RG_record_matrix, RB_matrix, RB_record_matrix, GB_matrix, GB_record_matrix = csv_operation.import_csv()

    image_recover_green=copy.deepcopy(image_remove_green)
    
    image_size = image_remove_green.shape

    #num_channel = image_size[2]
    num_row = image_size[0]  # how many rows
    num_column = image_size[1]  # how many columns
    
    #initialize recoverd_red to store
    recovered_green=np.zeros((num_row,num_column),dtype=np.int32)
    #for now, we recover the image except edge
    for i in np.arange(1, num_row - 1):
        for j in np.arange(1, num_column - 1):
            red_value = image_recover_green[i, j, 0]
            blue_value = image_recover_green[i, j, 2]

            red_contrast = pixel_operation.rms_contrast(image_recover_green, i, j, 0)
            blue_contrast = pixel_operation.rms_contrast(image_recover_green, i, j, 2)

            red_blue_contrast_mean = (red_contrast + blue_contrast) / 2
            
            RB_matrix_index = pixel_operation.contrast_index(red_blue_contrast_mean)
            
            recovered_green[i,j]=RB_matrix[blue_value,red_value,RB_matrix_index]
    
    image_recover_green[:,:,1]=recovered_green

    plt.imshow(image_recover_green)
    plt.xticks([])
    plt.yticks([])
    
    return image_recover_green
    

def recover_blue(image_remove_blue):
    RG_matrix, RG_record_matrix, RB_matrix, RB_record_matrix, GB_matrix, GB_record_matrix = csv_operation.import_csv()

    image_recover_blue=copy.deepcopy(image_remove_blue)
    
    image_size = image_remove_blue.shape

    #num_channel = image_size[2]
    num_row = image_size[0]  # how many rows
    num_column = image_size[1]  # how many columns
    
    #initialize recoverd_red to store
    recovered_blue=np.zeros((num_row,num_column),dtype=np.int32)
    #for now, we recover the image except edge
    for i in np.arange(1, num_row - 1):
        for j in np.arange(1, num_column - 1):
            red_value = image_recover_blue[i, j, 0]
            green_value = image_recover_blue[i, j, 1]

            red_contrast = pixel_operation.rms_contrast(image_recover_blue, i, j, 0)
            green_contrast = pixel_operation.rms_contrast(image_recover_blue, i, j, 1)

            red_green_contrast_mean = (red_contrast + green_contrast) / 2
            
            RG_matrix_index = pixel_operation.contrast_index(red_green_contrast_mean)
            
            recovered_blue[i,j]=RG_matrix[green_value,red_value,RG_matrix_index]
    
    image_recover_blue[:,:,2]=recovered_blue

    plt.imshow(image_recover_blue)
    plt.xticks([])
    plt.yticks([])
 
    return image_recover_blue
