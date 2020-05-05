#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:50:15 2020

@author: haoqiwang
"""

from matplotlib import pyplot as plt
import cv2
import imageio
import numpy as np
import os


def transform_image(image_path):
    # plt.imread(image_path)
    img16 = cv2.imread(image_path, -1)

    '''
    apply a sqrt transform. this approximates something called a 'gamma' transform. 
    it has to do with how monitors convert bits to light. 
    it is also why your image appears dark when you try to present 
    it on the screen. when you do the statistics, only do it on the image 
    BEFORE the sqrt transform. the sqrt transform is only necessary when 
    viewing the images on a monitor.
    '''

    '''
    img_scale=(img16.astype(np.float32))/(2**16-1)
    img_scale_gamma2=pow(img_scale,1/2)
    #img_scale_gamma2=img_scale
    img8_gamma2=np.uint8(img_scale_gamma2*(2**8-1))
    img8_gamma2 = cv2.cvtColor(img8_gamma2, cv2.COLOR_BGR2RGB)
    
    img_scale=(img16.astype(np.float32))/(2**16-1)
    img_scale_gamma3=pow(img_scale,1/3)
    img8_gamma3=np.uint8(img_scale_gamma3*(2**8-1))
    img8_gamma3 = cv2.cvtColor(img8_gamma3, cv2.COLOR_BGR2RGB)
    '''
    img8 = (img16 / 256).astype('uint8')
    img8 = cv2.cvtColor(img8, cv2.COLOR_BGR2RGB)
    # ii=img8-img8_gamma2

    # plt.imshow(img8)
    # plt.imshow(img8_gamma2)
    # plt.imshow(img8_gamma3)
    # plt.axis('off')

    # save unit8 image
    image_save_name = image_name[:-4] + '.jpg'
    imageio.imwrite(image_save_name, img8)
    # imageio.imwrite(image_save_name, img8_gamma2)
    # imageio.imwrite(image_save_name, img8_gamma3)

    # saved_image=plt.imread(image_save_name)
    # plt.imshow(saved_image)
    return


IMAGE_FOLDER = './image_database/'

# image_name = 'cps201004291795.ppm'
image_name_list = [name for name in os.listdir(IMAGE_FOLDER)]
image_name_list = list(filter(lambda image_name: image_name[-3:] == 'ppm', image_name_list))
for i in range(len(image_name_list)):
    image_name = image_name_list[i]
    image_path = IMAGE_FOLDER + image_name
    transform_image(image_path)
