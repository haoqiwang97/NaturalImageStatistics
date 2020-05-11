#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:34:08 2020

@author: haoqiwang
"""

# %matplotlib qt5
from lib import csv_operation

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

RG_no_contrast_matrix, RB_no_contrast_matrix, GB_no_contrast_matrix = csv_operation.import_csv_no_contrast()

# %%
fig = plt.figure(figsize=(8, 5))
ax = Axes3D(fig)
X = np.arange(256)
Y = 255 - np.arange(256)
X, Y = np.meshgrid(X, Y)
Z_GB_no_contrast = GB_no_contrast_matrix

# help(ax.plot_surface)
surf_red = ax.plot_surface(X, Y, Z_GB_no_contrast, cmap=plt.cm.Reds)
# ax.scatter(X, Y, Z_GB_no_contrast, cmap=plt.cm.Reds)

ax.set_zlabel('$\hat R_{opt}$')
ax.set_ylabel('B')
ax.set_xlabel('G')

fig.colorbar(surf_red, shrink=0.5, aspect=20)

# plt.savefig("predicted_red_no_contrast_surf", dpi=300)

plt.show()
# %%
fig = plt.figure()
ax = Axes3D(fig)
# X = np.arange(256)
# Y = np.arange(256)
# X, Y = np.meshgrid(X, Y)
Z_RB_no_contrast = RB_no_contrast_matrix

# help(ax.plot_surface)
surf_green = ax.plot_surface(X, Y, Z_RB_no_contrast, cmap=plt.cm.Greens)
# ax.scatter(X, Y, Z_GB_no_contrast, cmap=plt.cm.Reds)

ax.set_zlabel('$\hat G_{opt}$')
ax.set_ylabel('B')
ax.set_xlabel('R')

fig.colorbar(surf_green, shrink=0.5, aspect=20)

# plt.savefig("predicted_green_no_contrast_surf", dpi=300)

plt.show()
# %%
fig = plt.figure()
ax = Axes3D(fig)
# X = np.arange(256)
# Y = np.arange(256)
# X, Y = np.meshgrid(X, Y)
Z_RG_no_contrast = RG_no_contrast_matrix

# help(ax.plot_surface)
surf_blue = ax.plot_surface(X, Y, Z_RG_no_contrast, cmap=plt.cm.Blues)
# ax.scatter(X, Y, Z_GB_no_contrast, cmap=plt.cm.Reds)

ax.set_zlabel('$\hat B_{opt}$')
ax.set_ylabel('G')
ax.set_xlabel('R')

fig.colorbar(surf_blue, shrink=0.5, aspect=20)

# plt.savefig("predicted_blue_no_contrast_surf", dpi=300)

plt.show()
