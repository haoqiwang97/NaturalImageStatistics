#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:50:15 2020

@author: haoqiwang
"""

from lib import image_operation

from matplotlib import pyplot as plt

IMAGE_FOLDER = './image_database/'
image_name = 'cps201004291795.ppm'
image_name1 = 'natural_forest.jpg'

image_path = IMAGE_FOLDER + image_name
image_path1 = IMAGE_FOLDER + image_name1

ori_image = image_operation.read_image(image_path)
'''
import Image
im=Image.open(image_path)

from scipy.misc import imread
img = imread(image_path)
'''
import cv2
img16=cv2.imread(image_path,-1)
img8 = (img16/256).astype('uint8')
#plt.imshow(img8)
plt.imshow(cv2.cvtColor(img8, cv2.COLOR_BGR2RGB))

img22=cv2.imread(image_path1,-1)
#plt.imshow(img22)
plt.imshow(cv2.cvtColor(img22, cv2.COLOR_BGR2RGB))
img222=255-img8
plt.imshow(cv2.cvtColor(img222, cv2.COLOR_BGR2RGB))
#from scipy.misc import bytescale#cv2.imshow(image_path,0)
#max(im)
'''
import matplotlib.image as mpimg
img = mpimg.imread(image_path)
'''

#from PIL import Image
#im1 = Image.open(image_path)
