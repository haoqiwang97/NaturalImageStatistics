#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 22:57:18 2020

@author: haoqiwang
"""


import os
import pandas as pd
import numpy as np
'''
import all csv files

Example:

    RG_matrix,RG_record_matrix,RB_matrix,RB_record_matrix,GB_matrix,GB_record_matrix=csv_operation.import_csv()
'''

def import_csv():
    # csv location
    CSV_FOLDER = './train_database/'
    # get names for all images
    csv_name_list = [name for name in os.listdir(CSV_FOLDER)]
    
    # generate csv path
    csv_path_list=list(map(lambda csv_name:CSV_FOLDER+csv_name,csv_name_list))
    # seperate categories
    # TODO: 30 is magical number, perhaps find a way to deal with this
    #RG
    RG_csv_path_list=list(filter(lambda csv_name:csv_name[len(CSV_FOLDER):len(CSV_FOLDER)+2]=='RG' and len(csv_name)<30,csv_path_list))
    RG_csv_record_path_list=list(filter(lambda csv_name:csv_name[len(CSV_FOLDER):len(CSV_FOLDER)+2]=='RG' and len(csv_name)>30,csv_path_list))
    #RB
    RB_csv_path_list=list(filter(lambda csv_name:csv_name[len(CSV_FOLDER):len(CSV_FOLDER)+2]=='RB' and len(csv_name)<30,csv_path_list))
    RB_csv_record_path_list=list(filter(lambda csv_name:csv_name[len(CSV_FOLDER):len(CSV_FOLDER)+2]=='RB' and len(csv_name)>30,csv_path_list))
    #GB
    GB_csv_path_list=list(filter(lambda csv_name:csv_name[len(CSV_FOLDER):len(CSV_FOLDER)+2]=='GB' and len(csv_name)<30,csv_path_list))
    GB_csv_record_path_list=list(filter(lambda csv_name:csv_name[len(CSV_FOLDER):len(CSV_FOLDER)+2]=='GB' and len(csv_name)>30,csv_path_list))
    
    #generate 6 256*256*10 matrices to store opened csv
    num_row=256
    num_column=256
    num_contrast=10
    #RG
    RG_matrix=np.zeros((num_row,num_column,num_contrast),dtype=np.int32)
    RG_record_matrix=np.zeros((num_row,num_column,num_contrast),dtype=np.int32)
    #RB
    RB_matrix=np.zeros((num_row,num_column,num_contrast),dtype=np.int32)
    RB_record_matrix=np.zeros((num_row,num_column,num_contrast),dtype=np.int32)
    #GB
    GB_matrix=np.zeros((num_row,num_column,num_contrast),dtype=np.int32)
    GB_record_matrix=np.zeros((num_row,num_column,num_contrast),dtype=np.int32)
    
    '''
    # open each csv
    # store 60 csv in 6 arrays
    '''
    
    def df_formalize(csv_df):
        csv_df.drop(index=0, columns=0, inplace=True)
        csv_matrix=csv_df.to_numpy(dtype=np.int32)
        return csv_matrix
    
    #RG
    for RG_csv_path in RG_csv_path_list:
        RG_csv_df=pd.read_csv(RG_csv_path, header=None, names=None)
        RG_csv_matrix=df_formalize(RG_csv_df)
        RG_matrix[:,:,int(RG_csv_path[22])]=RG_csv_matrix #22 magical number, this is to extract the contrast index
    
    for RG_csv_record_path in RG_csv_record_path_list:
        RG_csv_record_df=pd.read_csv(RG_csv_record_path, header=None, names=None)
        RG_csv_record_matrix=df_formalize(RG_csv_record_df)
        RG_record_matrix[:,:,int(RG_csv_record_path[22])]=RG_csv_record_matrix #22 magical number, this is to extract the contrast index
    
    #RB
    for RB_csv_path in RB_csv_path_list:
        RB_csv_df=pd.read_csv(RB_csv_path, header=None, names=None)
        RB_csv_matrix=df_formalize(RB_csv_df)
        RB_matrix[:,:,int(RB_csv_path[22])]=RB_csv_matrix #22 magical number, this is to extract the contrast index
    
    for RB_csv_record_path in RB_csv_record_path_list:
        RB_csv_record_df=pd.read_csv(RB_csv_record_path, header=None, names=None)
        RB_csv_record_matrix=df_formalize(RB_csv_record_df)
        RB_record_matrix[:,:,int(RB_csv_record_path[22])]=RB_csv_record_matrix #22 magical number, this is to extract the contrast index
    
    #GB
    for GB_csv_path in GB_csv_path_list:
        GB_csv_df=pd.read_csv(GB_csv_path, header=None, names=None)
        GB_csv_matrix=df_formalize(GB_csv_df)
        GB_matrix[:,:,int(GB_csv_path[22])]=GB_csv_matrix #22 magical number, this is to extract the contrast index
    
    for GB_csv_record_path in GB_csv_record_path_list:
        GB_csv_record_df=pd.read_csv(GB_csv_record_path, header=None, names=None)
        GB_csv_record_matrix=df_formalize(GB_csv_record_df)
        GB_record_matrix[:,:,int(GB_csv_record_path[22])]=GB_csv_record_matrix #22 magical number, this is to extract the contrast index
    
    return RG_matrix,RG_record_matrix,RB_matrix,RB_record_matrix,GB_matrix,GB_record_matrix

