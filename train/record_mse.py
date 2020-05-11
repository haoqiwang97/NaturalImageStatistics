#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:00:48 2020

@author: haoqiwang
"""

from lib import csv_operation

import matplotlib.pyplot as plt
import numpy as np

RG_matrix, RG_record_matrix, RB_matrix, RB_record_matrix, GB_matrix, GB_record_matrix = csv_operation.import_csv()

num = RG_matrix.shape[2]

RG_mse = np.zeros(num)
RB_mse = np.zeros(num)
GB_mse = np.zeros(num)
for i in range(num):
    RG_mse[i] = np.var(RG_matrix[:, :, i])
    RB_mse[i] = np.var(RB_matrix[:, :, i])
    GB_mse[i] = np.var(GB_matrix[:, :, i])

x = np.linspace(0, 0.9, 10)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 4))
ax.plot(x, GB_mse, 'ro-', label='$\hat R_{MSE}$')
ax.plot(x, RB_mse, 'go-', label='$\hat G_{MSE}$')
ax.plot(x, RG_mse, 'bo-', label='$\hat B_{MSE}$')
ax.legend()
ax.set_xlabel('Mean Contrast')
ax.set_ylabel('MSE')

plt.savefig('MSE_contrast', dpi=300)
plt.show()
