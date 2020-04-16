#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 19:45:14 2020

@author: haoqiwang
"""
def red_contrast(image, i, j):
    r00 = image[i - 1, j - 1, 0]
    r01 = image[i - 1, j, 0]
    r02 = image[i - 1, j + 1, 0]

    r10 = image[i, j - 1, 0]
    r11 = image[i, j, 0]
    r12 = image[i, j + 1, 0]

    r20 = image[i + 1, j - 1, 0]
    r21 = image[i + 1, j, 0]
    r22 = image[i + 1, j + 1, 0]

    red_contrast_matrix = [r00, r01, r02, r10, r11, r12, r20, r21, r22]

    red_contrast = np.std(red_contrast_matrix) / np.mean(red_contrast_matrix)

    return red_contrast


def green_contrast(image, i, j):
    g00 = image[i - 1, j - 1, 1]
    g01 = image[i - 1, j, 1]
    g02 = image[i - 1, j + 1, 1]

    g10 = image[i, j - 1, 1]
    g11 = image[i, j, 1]
    g12 = image[i, j + 1, 1]

    g20 = image[i + 1, j - 1, 1]
    g21 = image[i + 1, j, 1]
    g22 = image[i + 1, j + 1, 1]

    green_contrast_matrix = [g00, g01, g02, g10, g11, g12, g20, g21, g22]

    green_contrast = np.std(green_contrast_matrix) / np.mean(green_contrast_matrix)

    return green_contrast


def blue_contrast(image, i, j):
    b00 = image[i - 1, j - 1, 2]
    b01 = image[i - 1, j, 2]
    b02 = image[i - 1, j + 1, 2]

    b10 = image[i, j - 1, 2]
    b11 = image[i, j, 2]
    b12 = image[i, j + 1, 2]

    b20 = image[i + 1, j - 1, 2]
    b21 = image[i + 1, j, 2]
    b22 = image[i + 1, j + 1, 2]

    blue_contrast_matrix = [b00, b01, b02, b10, b11, b12, b20, b21, b22]

    blue_contrast = np.std(blue_contrast_matrix) / np.mean(blue_contrast_matrix)

    return blue_contrast


red_contrast = red_contrast(image, i, j)
green_contrast = green_contrast(image, i, j)
blue_contrast = blue_contrast(image, i, j)