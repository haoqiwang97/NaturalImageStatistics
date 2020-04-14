#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:07:46 2020

@author: haoqiwang
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import copy

'''
example:
from utilities import remove_color
import matplotlib.image as mpimg
import numpy as np

filename='natural_forest.jpg'
ori_image = mpimg.imread(filename)
image = np.asarray(ori_image).astype(np.int32)

plt.imshow(image)
image_remove_red=remove_color.remove_red(image)
image_remove_green=remove_color.remove_green(image)
image_remove_blue=remove_color.remove_blue(image)
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
