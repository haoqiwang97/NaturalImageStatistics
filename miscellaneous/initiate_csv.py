'''
Generate csv files
30 files in total

file name rule:
RG_C00 means given Red, Green, contrast 0.0
RG_C01 means given Red, Green, contrast 0.1
...
RG_C09
10 files

RB_C00 means given Red, Blue, contrast 0.0
...
RB_C09
10 files

GB_C00 means given Green, Blue, contrast 0.0
...
GB_C09
10 files

30 files to record the number to calculate mean
RG_C00_record means the number of points given Red, Green, contrast 0.0

'''

import pandas as pd

df = pd.DataFrame()

for i in range(10):
    RG_filepath = './train_database/RG_C0' + str(i) + '.csv'
    RB_filepath = './train_database/RB_C0' + str(i) + '.csv'
    GB_filepath = './train_database/GB_C0' + str(i) + '.csv'
    
    RG_record_filepath='./train_database/RG_C0' + str(i) + '_record.csv'
    RB_record_filepath='./train_database/RB_C0' + str(i) + '_record.csv'
    GB_record_filepath='./train_database/GB_C0' + str(i) + '_record.csv'
    
    df.to_csv(RG_filepath)
    df.to_csv(RB_filepath)
    df.to_csv(GB_filepath)
    
    df.to_csv(RG_record_filepath)
    df.to_csv(RB_record_filepath)
    df.to_csv(GB_record_filepath)
