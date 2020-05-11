#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 19:48:27 2020

@author: haoqiwang
"""

from lib import csv_operation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
# %%
RG_no_contrast_matrix, RB_no_contrast_matrix, GB_no_contrast_matrix=csv_operation.import_csv_no_contrast()
# %%
# blue plot
# plt.imshow(RG_no_contrast, cmap=plt.cm.rainbow)
plt.imshow(RG_no_contrast, cmap=plt.cm.Blues)
plt.colorbar()
plt.title('$\hat B_{opt}$')
plt.xlabel('R')
plt.ylabel('G')

# plt.gca().invert_yaxis()
# plt.savefig("predicted_blue_no_contrast_rainbow", dpi=300)
# %%
# rainbow plot, fit the paper
# plt.imshow(RG_no_contrast, cmap=plt.cm.rainbow)
plt.imshow(RG_no_contrast, cmap=plt.cm.jet)
# plt.imshow(RG_no_contrast, cmap=plt.cm.Blues)
plt.colorbar()
plt.title('$\hat B_{opt}$')
plt.xlabel('R')
plt.ylabel('G')

plt.gca().invert_yaxis()
# plt.savefig("predicted_blue_no_contrast_jet", dpi=300)

# %%
# green plot
# plt.imshow(RB_no_contrast, cmap=plt.cm.rainbow)
plt.imshow(RB_no_contrast, cmap=plt.cm.Greens)
plt.colorbar()
plt.title('$\hat G_{opt}$')
plt.xlabel('R')
plt.ylabel('B')

# plt.gca().invert_yaxis()
# plt.savefig("predicted_green_no_contrast", dpi=300)
# %%
# rainbow plot, fit the paper
plt.imshow(RB_no_contrast.T, cmap=plt.cm.jet)
# plt.imshow(RB_no_contrast.T, cmap=plt.cm.rainbow)
# plt.imshow(RB_no_contrast, cmap=plt.cm.Greens)
plt.colorbar()
plt.title('$\hat G_{opt}$')
plt.xlabel('B')
plt.ylabel('R')

plt.gca().invert_yaxis()
# plt.savefig("predicted_green_no_contrast_rainbow", dpi=300)
# plt.savefig("predicted_green_no_contrast_jet", dpi=300)
# %%
# red plot
plt.imshow(GB_no_contrast, cmap=plt.cm.Reds)
plt.colorbar()
plt.title('$\hat R_{opt}$')
plt.xlabel('G')
plt.ylabel('B')
# plt.savefig("predicted_red_no_contrast", dpi=300)
# %%
# rainbow plot, fit the paper
plt.imshow(GB_no_contrast, cmap=plt.cm.rainbow)
# plt.imshow(GB_no_contrast, cmap=plt.cm.Reds)
plt.colorbar()
plt.title('$\hat R_{opt}$')
plt.xlabel('G')
plt.ylabel('B')

plt.gca().invert_yaxis()
# plt.savefig("predicted_red_no_contrast_rainbow", dpi=300)

