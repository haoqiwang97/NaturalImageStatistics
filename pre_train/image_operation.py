#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:17:35 2020

@author: haoqiwang
"""

import matplotlib.image as mpimg
import numpy as np


def read_image(image_path):
    ori_image = mpimg.imread(image_path)
    image = np.asarray(ori_image).astype(np.int32)
    return image
