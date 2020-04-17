#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:27:45 2020

@author: haoqiwang
"""

import csv_operation
import image_operation

import matplotlib.pyplot as plt
import numpy as np

RG_matrix, RG_record_matrix, RB_matrix, RB_record_matrix, GB_matrix, GB_record_matrix = csv_operation.import_csv()

image_path = './image_database/natural_forest.jpg'

image = image_operation.read_image(image_path)

plt.imshow(image)

RG_C00 = RG_matrix[:, :, 0]
plt.imshow(RG_matrix[:, :, 0], cmap=plt.cm.Blues)
plt.colorbar()

RB_C00 = RB_matrix[:, :, 0]
plt.imshow(RB_matrix[:, :, 0], cmap=plt.cm.Greens)
plt.colorbar()

GB_C00 = GB_matrix[:, :, 0]
plt.imshow(GB_matrix[:, :, 0], cmap=plt.cm.Reds)
plt.colorbar()

num_channel = 3
num_row = 256
# If we combine them
R_x_matrix = np.arange(0, num_row, dtype=np.int32).reshape(1, -1)
R_x_matrix = np.tile(R_x_matrix, (num_row, 1))

G_y_matrix = np.arange(0, num_row, dtype=np.int32).reshape(-1, 1)
G_y_matrix = np.tile(G_y_matrix, (1, num_row))

RG_C00_combine = np.zeros((num_row, num_row, num_channel), dtype=np.int32)
RG_C00_combine[:, :, 0] = R_x_matrix
RG_C00_combine[:, :, 1] = G_y_matrix
RG_C00_combine[:, :, 2] = RG_matrix[:, :, 0]

plt.imshow(RG_C00_combine)
