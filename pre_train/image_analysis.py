#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:17:48 2020

@author: haoqiwang
"""

import numpy as np
import os
import matplotlib.image as mpimg
import csv
import pandas as pd


def read_image(image_path):
    ori_image = mpimg.imread(image_path)
    image = np.asarray(ori_image).astype(np.int32)
    return image


def red_contrast(image, i, j):
    r00 = image[i - 1, j - 1, 0]
    r01 = image[i - 1, j, 0]
    r02 = image[i - 1, j + 1, 0]

    r10 = image[i, j - 1, 0]
    r11 = image[i, j, 0]
    r12 = image[i, j + 1, 0]

    r20 = image[i + 1, j - 1, 0]
    r21 = image[i + 1, j, 0]
    r22 = image[i + 1, j + 1, 0]

    red_contrast_matrix = [r00, r01, r02, r10, r11, r12, r20, r21, r22]

    red_contrast = np.std(red_contrast_matrix) / np.mean(red_contrast_matrix)

    # make contrast as 0,0.1,0.2,...,0.9
    return red_contrast


def green_contrast(image, i, j):
    g00 = image[i - 1, j - 1, 1]
    g01 = image[i - 1, j, 1]
    g02 = image[i - 1, j + 1, 1]

    g10 = image[i, j - 1, 1]
    g11 = image[i, j, 1]
    g12 = image[i, j + 1, 1]

    g20 = image[i + 1, j - 1, 1]
    g21 = image[i + 1, j, 1]
    g22 = image[i + 1, j + 1, 1]

    green_contrast_matrix = [g00, g01, g02, g10, g11, g12, g20, g21, g22]

    green_contrast = np.std(green_contrast_matrix) / np.mean(green_contrast_matrix)

    # make contrast as 0,0.1,0.2,...,0.9
    return green_contrast


def blue_contrast(image, i, j):
    b00 = image[i - 1, j - 1, 2]
    b01 = image[i - 1, j, 2]
    b02 = image[i - 1, j + 1, 2]

    b10 = image[i, j - 1, 2]
    b11 = image[i, j, 2]
    b12 = image[i, j + 1, 2]

    b20 = image[i + 1, j - 1, 2]
    b21 = image[i + 1, j, 2]
    b22 = image[i + 1, j + 1, 2]

    blue_contrast_matrix = [b00, b01, b02, b10, b11, b12, b20, b21, b22]

    blue_contrast = np.std(blue_contrast_matrix) / np.mean(blue_contrast_matrix)

    # make contrast as 0,0.1,0.2,...,0.9
    return blue_contrast


# def red_analysis(image):

IMAGE_FOLDER = './image_database/'  # image location

# get names for all images
image_name_list = [name for name in os.listdir(IMAGE_FOLDER)]

switch = {'0': red_analysis, '1': green_analysis, '2': blue_analysis}

for image_index in range(len(image_name_list)):
    image_name = image_name_list[image_index]
    image_path = IMAGE_FOLDER + image_name

    image = read_image(image_path)

    image_size = image.shape

    num_channel = image_size[2]
    num_row = image_size[0]  # how many rows
    num_column = image_size[1]  # how many columns

    i = 1
    j = 1
    # iterate each pixel except border
    for i in np.arange(1, num_row - 1):
        for j in np.arange(1, num_column - 1):
            # ith row, jth column pixel
            red_contrast = red_contrast(image, i, j)
            green_contrast = green_contrast(image, i, j)
            blue_contrast = blue_contrast(image, i, j)

            red_green_contrast_mean = (red_contrast + green_contrast) / 2
            red_blue_contrast_mean = (red_contrast + blue_contrast) / 2
            green_blue_contrast_mean = (green_contrast + blue_contrast) / 2

            # record the first 2 number as levels
            red_green_contrast_mean_str = str(red_green_contrast_mean)[:3]
            red_green_contrast_mean_str = red_green_contrast_mean_str[0] + red_green_contrast_mean_str[2]

            red_blue_contrast_mean_str = str(red_blue_contrast_mean)[:3]
            red_blue_contrast_mean_str = red_blue_contrast_mean_str[0] + red_blue_contrast_mean_str[2]

            green_blue_contrast_mean_str = str(green_blue_contrast_mean)[:3]
            green_blue_contrast_mean_str = green_blue_contrast_mean_str[0] + green_blue_contrast_mean_str[2]

            # go to the right csv(indicated by contrast) and extract the existing data
            # generate csv name
            RG_csv = "RG_C" + red_green_contrast_mean_str + ".csv"
            RG_record_csv = "RG_C" + red_green_contrast_mean_str + "_record" + ".csv"

            RB_csv = "RB_C" + red_blue_contrast_mean_str + ".csv"
            RB_record_csv = "RB_C" + red_blue_contrast_mean_str + "_record" + ".csv"

            GB_csv = "GB_C" + green_blue_contrast_mean_str + ".csv"
            GB_record_csv = "GB_C" + green_blue_contrast_mean_str + "_record" + ".csv"

            # read csv
            CSV_FOLDER = './train_database/'
            RG_csv_path = CSV_FOLDER + RG_csv

            RG_csv_df = pd.read_csv(RG_csv_path, header=None, names=None)

            # TODO: extract original value

            # input value as weighted outcome of original value and current value
            # TODO: remember now is 257*257

            # save csv file
            # extract row and column name

            column_name_list = RG_csv_df.iloc[:, 0]  # 第一列
            column_name_list = column_name_list.tolist()
            del column_name_list[0]

            row_name_list = RG_csv_df.iloc[0, :]  # 第一行
            row_name_list = row_name_list.tolist()
            del row_name_list[0]

            # RG_csv_df.drop(axis=0,index=None, columns=None, inplace=False)#delete first row
            RG_csv_df.drop(index=0, columns=None, inplace=True)  # delete first row
            RG_csv_df.drop(index=None, columns=0, inplace=True)  # delete first column

            RG_csv_df.columns = row_name_list
            RG_csv_df.index = column_name_list  # inverse, strange

            # RG_csv_df.to_csv('test.csv')
            RG_csv_df.to_csv(RG_csv_path)

            # locate row and column

            # write in new data

    for channel in range(num_channel):
        '''
        channel=0, red
        channel=1, green
        channel=2, blue
        '''
        switch.get(str(channel))()

CSV_FOLDER = './train_database/'
RG_csv_path = CSV_FOLDER + RG_csv
pd.read_csv()

with open(RG_csv_path) as csvfile:
    current_csv = csv.reader(csvfile)
    for row in f_csv:
        print(row)

current_csv['RG_C00_R_0', 'RG_C00_G_0']
RG_C00_R_0
RG_C00_G_0
