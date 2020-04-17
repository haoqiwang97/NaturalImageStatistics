#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:17:48 2020

@author: haoqiwang
"""

'''
This algorithm is too slow, because it has to open csv for every pixel,
every point needs 0.2s, I need to shorten this to 0.0001 or even 0.00001
'''

import numpy as np
import os
import matplotlib.image as mpimg

import pandas as pd
import datetime

from numba import jit


def read_image(image_path):
    ori_image = mpimg.imread(image_path)
    image = np.asarray(ori_image).astype(np.int32)
    return image


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

    contrast_matrix = [p00, p01, p02, p10, p11, p12, p20, p21, p22]

    rms_contrast = np.std(contrast_matrix) / np.mean(contrast_matrix)

    return rms_contrast


def pixel_analysis(image):
    global num_point
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
    for i in np.arange(1, 10 - 1):
        for j in np.arange(1, 10 - 1):
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

            # read csv, 6 csv to read
            CSV_FOLDER = './train_database/'

            RG_csv_path = CSV_FOLDER + RG_csv
            RB_csv_path = CSV_FOLDER + RB_csv
            GB_csv_path = CSV_FOLDER + GB_csv

            RG_record_csv_path = CSV_FOLDER + RG_record_csv
            RB_record_csv_path = CSV_FOLDER + RB_record_csv
            GB_record_csv_path = CSV_FOLDER + GB_record_csv

            RG_csv_df = pd.read_csv(RG_csv_path, header=None, names=None)
            RB_csv_df = pd.read_csv(RB_csv_path, header=None, names=None)
            GB_csv_df = pd.read_csv(GB_csv_path, header=None, names=None)

            RG_record_csv_df = pd.read_csv(RG_record_csv_path, header=None, names=None)
            RB_record_csv_df = pd.read_csv(RB_record_csv_path, header=None, names=None)
            GB_record_csv_df = pd.read_csv(GB_record_csv_path, header=None, names=None)

            '''
            locate row and column
            '''
            # RG
            RG_csv_row = 1 + green_value
            RG_csv_column = 1 + red_value

            # RB
            RB_csv_row = 1 + blue_value
            RB_csv_column = 1 + red_value

            # GB
            GB_csv_row = 1 + blue_value
            GB_csv_column = 1 + green_value

            '''
            extract original value
            '''
            # RG
            RG_csv_df_cell = int(RG_csv_df.iloc[RG_csv_row, RG_csv_column])
            RG_record_csv_df_cell = int(RG_record_csv_df.iloc[RG_csv_row, RG_csv_column])

            # RB
            RB_csv_df_cell = int(RB_csv_df.iloc[RB_csv_row, RB_csv_column])
            RB_record_csv_df_cell = int(RB_record_csv_df.iloc[RB_csv_row, RB_csv_column])

            # GB
            GB_csv_df_cell = int(GB_csv_df.iloc[GB_csv_row, GB_csv_column])
            GB_record_csv_df_cell = int(GB_record_csv_df.iloc[GB_csv_row, GB_csv_column])

            '''
            update value as weighted outcome of original value and current value
            '''
            # RG
            RG_csv_df_cell = int((RG_csv_df_cell * RG_record_csv_df_cell + blue_value) / (RG_record_csv_df_cell + 1))
            RG_record_csv_df_cell = int(RG_record_csv_df_cell + 1)

            # RB
            RB_csv_df_cell = int((RB_csv_df_cell * RB_record_csv_df_cell + green_value) / (RB_record_csv_df_cell + 1))
            RB_record_csv_df_cell = int(RB_record_csv_df_cell + 1)

            # GB
            GB_csv_df_cell = int((GB_csv_df_cell * GB_record_csv_df_cell + red_value) / (GB_record_csv_df_cell + 1))
            GB_record_csv_df_cell = int(GB_record_csv_df_cell + 1)

            '''
            input value
            '''
            # RG
            RG_csv_df.iloc[RG_csv_row, RG_csv_column] = RG_csv_df_cell
            RG_record_csv_df.iloc[RG_csv_row, RG_csv_column] = RG_record_csv_df_cell

            # RB
            RB_csv_df.iloc[RB_csv_row, RB_csv_column] = RB_csv_df_cell
            RB_record_csv_df.iloc[RB_csv_row, RB_csv_column] = RB_record_csv_df_cell

            # GB
            GB_csv_df.iloc[GB_csv_row, GB_csv_column] = GB_csv_df_cell
            GB_record_csv_df.iloc[GB_csv_row, GB_csv_column] = GB_record_csv_df_cell

            # save csv file
            # extract row and column name

            '''
            formalize dataframe
            '''
            # RG
            RG_column_name_list = RG_csv_df.iloc[:, 0]  # first column
            RG_column_name_list = RG_column_name_list.tolist()
            del RG_column_name_list[0]

            RG_row_name_list = RG_csv_df.iloc[0, :]  # first row
            RG_row_name_list = RG_row_name_list.tolist()
            del RG_row_name_list[0]

            RG_record_column_name_list = RG_record_csv_df.iloc[:, 0]  # first column
            RG_record_column_name_list = RG_record_column_name_list.tolist()
            del RG_record_column_name_list[0]

            RG_record_row_name_list = RG_record_csv_df.iloc[0, :]  # first row
            RG_record_row_name_list = RG_record_row_name_list.tolist()
            del RG_record_row_name_list[0]

            RG_csv_df.drop(index=0, columns=None, inplace=True)  # delete first row
            RG_csv_df.drop(index=None, columns=0, inplace=True)  # delete first column

            RG_record_csv_df.drop(index=0, columns=None, inplace=True)  # delete first row
            RG_record_csv_df.drop(index=None, columns=0, inplace=True)  # delete first column

            RG_csv_df.columns = RG_row_name_list
            RG_csv_df.index = RG_column_name_list  # inverse, strange

            RG_record_csv_df.columns = RG_row_name_list
            RG_record_csv_df.index = RG_column_name_list

            # RB
            RB_column_name_list = RB_csv_df.iloc[:, 0]  # first column
            RB_column_name_list = RB_column_name_list.tolist()
            del RB_column_name_list[0]

            RB_row_name_list = RB_csv_df.iloc[0, :]  # first row
            RB_row_name_list = RB_row_name_list.tolist()
            del RB_row_name_list[0]

            RB_record_column_name_list = RB_record_csv_df.iloc[:, 0]  # first column
            RB_record_column_name_list = RB_record_column_name_list.tolist()
            del RB_record_column_name_list[0]

            RB_record_row_name_list = RB_record_csv_df.iloc[0, :]  # first row
            RB_record_row_name_list = RB_record_row_name_list.tolist()
            del RB_record_row_name_list[0]

            RB_csv_df.drop(index=0, columns=None, inplace=True)  # delete first row
            RB_csv_df.drop(index=None, columns=0, inplace=True)  # delete first column

            RB_record_csv_df.drop(index=0, columns=None, inplace=True)  # delete first row
            RB_record_csv_df.drop(index=None, columns=0, inplace=True)  # delete first column

            RB_csv_df.columns = RB_row_name_list
            RB_csv_df.index = RB_column_name_list  # inverse, strange

            RB_record_csv_df.columns = RB_row_name_list
            RB_record_csv_df.index = RB_column_name_list

            # GB
            GB_column_name_list = GB_csv_df.iloc[:, 0]  # first column
            GB_column_name_list = GB_column_name_list.tolist()
            del GB_column_name_list[0]

            GB_row_name_list = GB_csv_df.iloc[0, :]  # first row
            GB_row_name_list = GB_row_name_list.tolist()
            del GB_row_name_list[0]

            GB_record_column_name_list = GB_record_csv_df.iloc[:, 0]  # first column
            GB_record_column_name_list = GB_record_column_name_list.tolist()
            del GB_record_column_name_list[0]

            GB_record_row_name_list = GB_record_csv_df.iloc[0, :]  # first row
            GB_record_row_name_list = GB_record_row_name_list.tolist()
            del GB_record_row_name_list[0]

            GB_csv_df.drop(index=0, columns=None, inplace=True)  # delete first row
            GB_csv_df.drop(index=None, columns=0, inplace=True)  # delete first column

            GB_record_csv_df.drop(index=0, columns=None, inplace=True)  # delete first row
            GB_record_csv_df.drop(index=None, columns=0, inplace=True)  # delete first column

            GB_csv_df.columns = GB_row_name_list
            GB_csv_df.index = GB_column_name_list  # inverse, strange

            GB_record_csv_df.columns = GB_row_name_list
            GB_record_csv_df.index = GB_column_name_list

            '''
            write in new data
            '''
            # RG
            # RG_csv_df.to_csv('test.csv')
            RG_csv_df.to_csv(RG_csv_path)
            RG_record_csv_df.to_csv(RG_record_csv_path)

            # RB
            RB_csv_df.to_csv(RB_csv_path)
            RB_record_csv_df.to_csv(RB_record_csv_path)

            # GB
            GB_csv_df.to_csv(GB_csv_path)
            GB_record_csv_df.to_csv(GB_record_csv_path)

            num_point += 1
    return


IMAGE_FOLDER = './image_database/'  # image location

# get names for all images
image_name_list = [name for name in os.listdir(IMAGE_FOLDER)]

# @jit(nopython=True,nogil=True)
# iterate pixels
for image_index in range(len(image_name_list)):
    t1 = datetime.datetime.now()  # start stopwatch

    image_name = image_name_list[image_index]
    image_path = IMAGE_FOLDER + image_name

    image = read_image(image_path)
    pixel_analysis(image)

    t2 = datetime.datetime.now()

    time_elapse = t2 - t1

    print('The number of image: ' + str(image_index))
    print('Image name: ' + image_name)
    print('time elapse =', time_elapse)
    print('\n')

    file = open("./record/test.txt", "a")
    # file.writelines('@jit(nopython=True,nogil=True)')
    # file.writelines('\n')

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
