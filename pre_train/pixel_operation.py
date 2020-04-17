#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:42:08 2020

@author: haoqiwang
"""

import numpy as np

from numba import jit


@jit(nopython=True, nogil=True)
def rms_contrast(image, i, j, channel):
    p00 = image[i - 1, j - 1, channel]
    p01 = image[i - 1, j, channel]
    p02 = image[i - 1, j + 1, channel]

    p10 = image[i, j - 1, channel]
    p11 = image[i, j, channel]
    p12 = image[i, j + 1, channel]

    p20 = image[i + 1, j - 1, channel]
    p21 = image[i + 1, j, channel]
    p22 = image[i + 1, j + 1, channel]

    # contrast_matrix = [p00, p01, p02, p10, p11, p12, p20, p21, p22]

    contrast_matrix = np.array([p00, p01, p02, p10, p11, p12, p20, p21, p22], dtype=np.float32)

    rms_contrast = np.std(contrast_matrix) / np.mean(contrast_matrix)

    return rms_contrast


@jit(nopython=True, nogil=True)
def contrast_index(contrast_mean):
    # because little error or approximation during rms_contrast, some contrast value may slightly greater than 1
    if contrast_mean < 1:
        return int(contrast_mean * 10)
    else:
        return int(9)


@jit(nopython=True, nogil=True)
def pixel_analysis(image, RG_matrix, RG_record_matrix, RB_matrix, RB_record_matrix, GB_matrix, GB_record_matrix):
    num_point = 0

    image_size = image.shape

    num_channel = image_size[2]
    num_row = image_size[0]  # how many rows
    num_column = image_size[1]  # how many columns

    # i = 1
    # j = 1
    # iterate each pixel except border
    # for i in np.arange(1, num_row - 1):
    # for j in np.arange(1, num_column - 1):
    for i in np.arange(1, num_row - 1):
        for j in np.arange(1, num_column - 1):
            # print(i, j)
            # ith row, jth column pixel
            red_value = image[i, j, 0]
            green_value = image[i, j, 1]
            blue_value = image[i, j, 2]

            red_contrast = rms_contrast(image, i, j, 0)
            green_contrast = rms_contrast(image, i, j, 1)
            blue_contrast = rms_contrast(image, i, j, 2)

            red_green_contrast_mean = (red_contrast + green_contrast) / 2
            red_blue_contrast_mean = (red_contrast + blue_contrast) / 2
            green_blue_contrast_mean = (green_contrast + blue_contrast) / 2

            # red_green_contrast_mean = red_green_contrast_mean.astype(np.float16)
            # red_blue_contrast_mean = red_blue_contrast_mean.astype(np.float16)
            # green_blue_contrast_mean = green_blue_contrast_mean.astype(np.float16)

            # RG
            # RG_matrix_index = int(str(red_green_contrast_mean)[2])#the string makes us cannot apply numba to accelerate
            # RG_matrix_index = int(red_green_contrast_mean*10)
            RG_matrix_index = contrast_index(red_green_contrast_mean)

            # extract origianl values
            RG_matrix_cell = RG_matrix[green_value, red_value, RG_matrix_index]
            RG_record_matrix_cell = RG_record_matrix[green_value, red_value, RG_matrix_index]
            # update value
            RG_matrix[green_value, red_value, RG_matrix_index] = int(
                (RG_matrix_cell * RG_record_matrix_cell + blue_value) / (RG_record_matrix_cell + 1))
            RG_record_matrix[green_value, red_value, RG_matrix_index] = int(RG_record_matrix_cell + 1)

            # RB
            # RB_matrix_index = int(str(red_blue_contrast_mean)[2])
            # print('red_blue_contrast_mean',red_blue_contrast_mean)
            # RB_matrix_index = int(red_blue_contrast_mean*10)
            # print('RB_matrix_index: ',RB_matrix_index)
            RB_matrix_index = contrast_index(red_blue_contrast_mean)

            # extract origianl values
            RB_matrix_cell = RB_matrix[blue_value, red_value, RB_matrix_index]
            RB_record_matrix_cell = RB_record_matrix[blue_value, red_value, RB_matrix_index]
            # update value
            RB_matrix[blue_value, red_value, RB_matrix_index] = int(
                (RB_matrix_cell * RB_record_matrix_cell + green_value) / (RB_record_matrix_cell + 1))
            RB_record_matrix[blue_value, red_value, RB_matrix_index] = int(RB_record_matrix_cell + 1)

            # GB
            # GB_matrix_index = int(str(green_blue_contrast_mean)[2])
            # GB_matrix_index = int(green_blue_contrast_mean*10)
            GB_matrix_index = contrast_index(green_blue_contrast_mean)

            # extract origianl values
            GB_matrix_cell = GB_matrix[blue_value, green_value, GB_matrix_index]
            GB_record_matrix_cell = GB_record_matrix[blue_value, green_value, GB_matrix_index]
            # update value
            GB_matrix[blue_value, green_value, GB_matrix_index] = int(
                (GB_matrix_cell * GB_record_matrix_cell + red_value) / (GB_record_matrix_cell + 1))
            GB_record_matrix[blue_value, green_value, GB_matrix_index] = int(GB_record_matrix_cell + 1)

            num_point += 1

    return num_point, RG_matrix, RG_record_matrix, RB_matrix, RB_record_matrix, GB_matrix, GB_record_matrix
