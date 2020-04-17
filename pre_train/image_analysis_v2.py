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

import csv_operation

RG_matrix,RG_record_matrix,RB_matrix,RB_record_matrix,GB_matrix,GB_record_matrix=csv_operation.import_csv()
