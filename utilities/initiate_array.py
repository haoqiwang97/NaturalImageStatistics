# TODO: initiate 256*256*10*? array to store the predicted color, which can be multiple

# TODO: initiate 256*256*10 array to store mean of predicted color channel

# TODO: NOT possible to store the value in memory, that is too large, write it in excel or csv

# TODO: an excel for a color, containing 10 sheets, or maybe 20 (another sheet is for the number, to calculate mean)
#  , each sheet represents a level of contrast, so we just add them and then calculate mean

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
'''

import pandas as pd

df = pd.DataFrame()

for i in range(10):
    RG_filepath = './train_database/RG_C0' + str(i) + '.csv'
    RB_filepath = './train_database/RB_C0' + str(i) + '.csv'
    GB_filepath = './train_database/GB_C0' + str(i) + '.csv'
    df.to_csv(RG_filepath)
    df.to_csv(RB_filepath)
    df.to_csv(GB_filepath)
