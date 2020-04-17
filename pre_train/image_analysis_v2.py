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
import pandas as pd
import numpy as np
'''
import all csv files
'''
# csv location
CSV_FOLDER = './train_database/'
# get names for all images
csv_name_list = [name for name in os.listdir(CSV_FOLDER)]

# generate csv path
csv_path_list=list(map(lambda csv_name:CSV_FOLDER+csv_name,csv_name_list))
# seperate categories
# TODO: 30 is magical number, perhaps find a way to deal with this
RG_csv_path_list=list(filter(lambda csv_name:csv_name[len(CSV_FOLDER):len(CSV_FOLDER)+2]=='RG' and len(csv_name)<30,csv_path_list))
RG_csv_record_path_list=list(filter(lambda csv_name:csv_name[len(CSV_FOLDER):len(CSV_FOLDER)+2]=='RG' and len(csv_name)>30,csv_path_list))
# TODO: for rb, gb

#generate 6 256*256*10 matrices to store opened csv
num_row=256
num_column=256
num_contrast=10
RG_matrix=np.zeros((num_row,num_column,num_contrast),dtype=np.int32)
RG_record_matrix=np.zeros((num_row,num_column,num_contrast),dtype=np.int32)
# TODO: for rb, gb
# open each csv


def df_formalize(csv_df):
    csv_df.drop(index=0, columns=0, inplace=True)
    csv_matrix=csv_df.to_numpy(dtype=np.int32)
    return csv_matrix

for RG_csv_path in RG_csv_path_list:
    RG_csv_df=pd.read_csv(RG_csv_path, header=None, names=None)
    RG_csv_matrix=df_formalize(RG_csv_df)
    RG_matrix[:,:,int(RG_csv_path[22])]=RG_csv_matrix #22 magical number, this is to extract the contrast index











csv_path='./train_database/RG_C00.csv'
int(csv_path[17])
int(csv_path[22])
len(CSV_FOLDER)
len(csv_path)

RG_csv_df.to_numpy(dtype=np.int32)

#list(map(lambda RG_csv_df:RG_csv_df.drop(index=0, columns=0, inplace=True),pd.read_csv('./train_database/RG_C00.csv', header=None, names=None)))



#RG_csv_df=pd.read_csv('./train_database/RG_C00.csv', header=0, names=0)

RG_csv_df.drop(index=0, columns=0, inplace=True)  # delete first row
RG_csv_df.drop(index=None, columns=0, inplace=True)  # delete first column


'./train_database/RG_C00.csv'
csv=pd.read_csv('./train_database/GB_C08_record.csv', header=None, names=None)

# store 60 csv in 6 arrays

dtype=np.int32

xx='RG_C01.csv'
xx[0:2]
len(csv_path_list)

