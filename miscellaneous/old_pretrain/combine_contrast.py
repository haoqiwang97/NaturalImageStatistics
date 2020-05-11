#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:48:27 2020

@author: haoqiwang
"""

from lib import csv_operation

import numpy as np
import pandas as pd

RG_matrix, RG_record_matrix, RB_matrix, RB_record_matrix, GB_matrix, GB_record_matrix = csv_operation.import_csv()

CSV_FOLDER = './train_database_no_contrast/'

RG_no_contrast = csv_operation.combine_contrast(RG_matrix, RG_record_matrix)
RB_no_contrast = csv_operation.combine_contrast(RB_matrix, RB_record_matrix)
GB_no_contrast = csv_operation.combine_contrast(GB_matrix, GB_record_matrix)

'''
RG_no_contrast_df = pd.DataFrame(RG_no_contrast, dtype=np.int32)
RG_no_contrast_df.to_csv(CSV_FOLDER + 'RG_no_contrast' + '.csv')

RB_no_contrast_df = pd.DataFrame(RB_no_contrast, dtype=np.int32)
RB_no_contrast_df.to_csv(CSV_FOLDER + 'RB_no_contrast' + '.csv')

GB_no_contrast_df = pd.DataFrame(GB_no_contrast, dtype=np.int32)
GB_no_contrast_df.to_csv(CSV_FOLDER + 'GB_no_contrast' + '.csv')
'''
