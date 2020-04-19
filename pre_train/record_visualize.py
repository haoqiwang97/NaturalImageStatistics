#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:27:45 2020

@author: haoqiwang
"""

from lib import csv_operation
from lib import image_operation

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

RG_matrix, RG_record_matrix, RB_matrix, RB_record_matrix, GB_matrix, GB_record_matrix = csv_operation.import_csv()

IMAGE_FOLDER = './image_database/'
image_name = 'natural_forest.jpg'

image_path = IMAGE_FOLDER + image_name

image = image_operation.read_image(image_path)

plt.imshow(image)
# %%
# plot predicted blue
num_row = 2
num_column = 5
num = 0
fig, axes = plt.subplots(nrows=num_row, ncols=num_column, figsize=(12.5, 5))

images = []
for i in range(num_row):
    for j in range(num_column):
        img = axes[i, j].imshow(RG_matrix[:, :, num], cmap=plt.cm.Blues)
        axes[i, j].set_title('$\hat B_{opt}$, $C_{RG}=0.%d$' % (num))
        axes[i, j].set_xlabel('R')
        axes[i, j].set_ylabel('G')

        images.append(img)
        axes[i, j].label_outer()
        num += 1

# Find the min and max of all colors for use in setting the color scale.
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

fig.colorbar(images[0], ax=axes, orientation='vertical', fraction=.05)

# fig.tight_layout()

plt.savefig("natural_forest_predicted_blue", dpi=300)

plt.show()
# %%
# plot predicted green
num_row = 2
num_column = 5
num = 0
fig, axes = plt.subplots(nrows=num_row, ncols=num_column, figsize=(12.5, 5))

images = []
for i in range(num_row):
    for j in range(num_column):
        img = axes[i, j].imshow(RB_matrix[:, :, num], cmap=plt.cm.Greens)
        axes[i, j].set_title('$\hat G_{opt}$, $C_{RB}=0.%d$' % (num))
        axes[i, j].set_xlabel('R')
        axes[i, j].set_ylabel('B')

        images.append(img)
        axes[i, j].label_outer()
        num += 1

# Find the min and max of all colors for use in setting the color scale.
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

fig.colorbar(images[0], ax=axes, orientation='vertical', fraction=.05)

# fig.tight_layout()

plt.savefig("natural_forest_predicted_green", dpi=300)

plt.show()
# %%
# plot predicted red
num_row = 2
num_column = 5
num = 0
fig, axes = plt.subplots(nrows=num_row, ncols=num_column, figsize=(12.5, 5))
# fig.suptitle('')

images = []
for i in range(num_row):
    for j in range(num_column):
        img = axes[i, j].imshow(GB_matrix[:, :, num], cmap=plt.cm.Reds)
        axes[i, j].set_title('$\hat R_{opt}$, $C_{GB}=0.%d$' % (num))
        axes[i, j].set_xlabel('G')
        axes[i, j].set_ylabel('B')

        images.append(img)
        axes[i, j].label_outer()
        num += 1

# Find the min and max of all colors for use in setting the color scale.
vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin=vmin, vmax=vmax)
for im in images:
    im.set_norm(norm)

fig.colorbar(images[0], ax=axes, orientation='vertical', fraction=.05)

# fig.tight_layout()

# plt.savefig("natural_forest_predicted_red",dpi=300)

plt.show()
# %%
# trail
RG_C00 = RG_matrix[:, :, 0]
plt.imshow(RG_matrix[:, :, 0], cmap=plt.cm.Blues)
plt.colorbar()

RB_C00 = RB_matrix[:, :, 0]
plt.imshow(RB_matrix[:, :, 0], cmap=plt.cm.Greens)
plt.colorbar()

GB_C00 = GB_matrix[:, :, 0]
plt.imshow(GB_matrix[:, :, 0], cmap=plt.cm.Reds)
plt.colorbar()

# %%
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
