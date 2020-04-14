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

'''
Generate sheet in each csv files

columns/rows name rule:
RG_C00 means given Red, Green, contrast 0.0
256 columns, 256 rows
columns: RG_C00_R_0, RG_C00_R_1, ... RG_C00_R_255
rows: RG_C00_G_0, RG_C00_G_1, ... RG_C00_G_255

RG_C00_record means the number of points given Red, Green, contrast 0.0
256 columns, 256 rows
columns: RG_C00_record_R_0, RG_C00_record_R_1, ... RG_C00_record_R_255
rows: RG_C00_record_G_0, RG_C00_record_G_1, ... RG_C00_record_G_255
'''
import numpy as np
import pandas as pd

def generate_filename_list(num_contrast):
    filename_list=[]
    for i in range(num_contrast):
        RG_filename='RG_C0' + str(i)
        RB_filename='RB_C0' + str(i)
        GB_filename='GB_C0' + str(i)
        RG_record_filename='RG_C0' + str(i)+'_record'
        RB_record_filename='RB_C0' + str(i)+'_record'
        GB_record_filename='GB_C0' + str(i)+'_record'
        
        filename_list.append(RG_filename)
        filename_list.append(RG_record_filename)
        
        filename_list.append(RB_filename)
        filename_list.append(RB_record_filename)
        
        filename_list.append(GB_filename)
        filename_list.append(GB_record_filename)

    return filename_list

def generate_csv(filename):
    
    df = pd.DataFrame(np.zeros((num_row,num_column),dtype=np.int32))
    
    def column_row_name(filename):
        #generate columns and rows names
        #generate a 256*256 all 0 matrix
        column_name_list=np.zeros(num_column,dtype=object)
        row_name_list=np.zeros(num_row,dtype=object)
        for i in range(num_column):
            column_name=filename+'_'+filename[0]+'_'+str(i)
            column_name_list[i]=column_name
            row_name=filename+'_'+filename[1]+'_'+str(i)
            row_name_list[i]=row_name
        return column_name_list,row_name_list
    
    column_name_list,row_name_list=column_row_name(filename) 
    
    df.columns=column_name_list#set names of columns
    df.index=row_name_list#set names of rows
    return df

filepath = './train_database/'

num_row=256#number of rows
num_column=256#number of columns
num_contrast=10#10 levels of contrast

filename_list=generate_filename_list(num_contrast)

filename = pd.DataFrame(filename_list)
filename.to_csv(filepath+'filename_list'+'.csv')#store filename_list

for filename in filename_list:
    df=generate_csv(filename)
    df.to_csv(filepath+filename+'.csv')





