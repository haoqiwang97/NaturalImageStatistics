#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 14:25:35 2020

@author: haoqiwang
"""

from itertools import product
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C, WhiteKernel

X = np.array([[0, 0], [2, 0], [4, 0], [6, 0], [8, 0], [10, 0], [12, 0], [14, 0], [16, 0], [0, 2],
              [2, 2], [4, 2], [6, 2], [8, 2], [10, 2], [12, 2], [14, 2], [16, 2]])

y = np.array([-54, -60, -62, -64, -66, -68, -70, -72, -74, -60, -62, -64, -66,
              -68, -70, -72, -74, -76])

# kernel = C(1.0, (1e-3, 1e3)) * RBF([5,5], (1e-2, 1e2))
kernel = C(1.0, (1e-3, 1e3)) * RBF(1.0, (1e-2, 1e2)) + WhiteKernel(1.0, (1e-5, 1e2))
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=15)

gp.fit(X, y)

# Input space
x1 = np.linspace(X[:, 0].min(), X[:, 0].max())  # p
x2 = np.linspace(X[:, 1].min(), X[:, 1].max())  # q
x = (np.array([x1, x2])).T
x1x2 = np.array(list(product(x1, x2)))
y_pred, MSE = gp.predict(x1x2, return_std=True)

X0p, X1p = x1x2[:, 0].reshape(50, 50), x1x2[:, 1].reshape(50, 50)

Zp = np.reshape(y_pred, (50, 50))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X0p, X1p, Zp, rstride=1, cstride=1, cmap='jet', linewidth=0, antialiased=False)

gp.kernel_.k1.get_params()
gp.kernel_.k1.get_params()['k1__constant_value']

gp.kernel_.k2.get_params()
