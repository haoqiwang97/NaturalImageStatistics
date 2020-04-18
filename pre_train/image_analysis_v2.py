#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:57:18 2020

@author: haoqiwang
"""

'''
2nd version of image_analysis
I will try to write that opening csv for each image to help speed up
'''
import os
import datetime

from lib import csv_operation
from lib import pixel_operation
from lib import image_operation

IMAGE_FOLDER = './image_database/'  # image location

# get names for all images
image_name_list = [name for name in os.listdir(IMAGE_FOLDER)]
# image_index=0
for image_index in range(len(image_name_list)):
    image_name = image_name_list[image_index]
    image_path = IMAGE_FOLDER + image_name
    # start stopwatch
    t1 = datetime.datetime.now()

    RG_matrix, RG_record_matrix, RB_matrix, RB_record_matrix, GB_matrix, GB_record_matrix = csv_operation.import_csv()

    image = image_operation.read_image(image_path)

    num_point, RG_matrix, RG_record_matrix, RB_matrix, RB_record_matrix, GB_matrix, GB_record_matrix = pixel_operation.pixel_analysis(
        image, RG_matrix, RG_record_matrix, RB_matrix, RB_record_matrix, GB_matrix, GB_record_matrix)

    csv_operation.export_csv(RG_matrix, RG_record_matrix, RB_matrix, RB_record_matrix, GB_matrix, GB_record_matrix)

    t2 = datetime.datetime.now()

    time_elapse = t2 - t1

    print('The number of image: ' + str(image_index))
    print('Image name: ' + image_name)
    print('time elapse =', time_elapse)
    print('\n')

    file = open("./record/test.txt", "a")

    file.writelines('Date time: ' + str(datetime.datetime.now()))
    file.writelines('\n')

    file.writelines('@jit(nopython=True,nogil=True)')
    file.writelines('\n')

    file.writelines('The number of image: ' + str(image_index))
    file.writelines('\n')
    file.writelines('Image name: ' + image_name)
    file.writelines('\n')
    file.writelines('Image dimension: ' + str(image.shape[0]) + '*' + str(image.shape[1]))
    file.writelines('\n')
    file.writelines('Total number of pixels: ' + str(image.shape[0] * image.shape[1]))
    file.writelines('\n')
    file.writelines('Total number of trained points: ' + str(num_point))
    file.writelines('\n')
    file.writelines('time elapse =' + str(time_elapse))
    file.writelines('\n')
    file.writelines('\n')

    file.close()
