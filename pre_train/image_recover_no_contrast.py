#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:23:48 2020

@author: haoqiwang
"""

from lib import image_operation

IMAGE_FOLDER = './image_database/'
image_name = 'natural_forest.jpg'

image_path = IMAGE_FOLDER + image_name

# red
ori_image = image_operation.read_image(image_path)
image_remove_red = image_operation.remove_red(ori_image)

image_recover_red = image_operation.recover_red(image_remove_red)
image_recover_red_no_contrast = image_operation.recover_red_no_contrast(image_remove_red)

mse_red = image_operation.compare_image(ori_image, image_recover_red)
mse_red_no_contrast = image_operation.compare_image(ori_image, image_recover_red_no_contrast)

# green
ori_image = image_operation.read_image(image_path)
image_remove_green = image_operation.remove_green(ori_image)

image_recover_green = image_operation.recover_green(image_remove_green)
image_recover_green_no_contrast = image_operation.recover_green_no_contrast(image_remove_green)

mse_green = image_operation.compare_image(ori_image, image_recover_green)
mse_green_no_contrast = image_operation.compare_image(ori_image, image_recover_green_no_contrast)

# blue
ori_image = image_operation.read_image(image_path)
image_remove_blue = image_operation.remove_blue(ori_image)

image_recover_blue = image_operation.recover_blue(image_remove_blue)
image_recover_blue_no_contrast = image_operation.recover_blue_no_contrast(image_remove_blue)

mse_blue = image_operation.compare_image(ori_image, image_recover_blue)
mse_blue_no_contrast = image_operation.compare_image(ori_image, image_recover_blue_no_contrast)
