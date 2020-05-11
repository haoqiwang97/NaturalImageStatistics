#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:25:27 2020

@author: haoqiwang
"""

from lib import image_operation

from matplotlib import pyplot as plt

# IMAGE_FOLDER = './test_images/'
IMAGE_FOLDER = './image_database/'
# image_name = 'cps201004281214.jpg'
# image_name = 'cps201004281763.jpg'
# image_name = 'cps201010123990.jpg'
# image_name = 'cps201010083774.jpg'
# image_name = 'cps201004291795.jpg'
image_name = 'natural_forest.jpg'
image_path = IMAGE_FOLDER + image_name
# %%
# remove and recover red
ori_image = image_operation.read_image(image_path)
image_remove_red = image_operation.remove_red(ori_image)
image_recover_red = image_operation.recover_red(image_remove_red)

image_recover_red_no_contrast = image_operation.recover_red_no_contrast(image_remove_red)

mse_red = image_operation.compare_image(ori_image, image_recover_red)
mse_red_no_contrast = image_operation.compare_image(ori_image, image_recover_red_no_contrast)

# %%
# remove and recover green
ori_image = image_operation.read_image(image_path)
image_remove_green = image_operation.remove_green(ori_image)
image_recover_green = image_operation.recover_green(image_remove_green)

image_recover_green_no_contrast = image_operation.recover_green_no_contrast(image_remove_green)

mse_green = image_operation.compare_image(ori_image, image_recover_green)
mse_green_no_contrast = image_operation.compare_image(ori_image, image_recover_green_no_contrast)

# %%
# remove and recover blue
ori_image = image_operation.read_image(image_path)
image_remove_blue = image_operation.remove_blue(ori_image)
image_recover_blue = image_operation.recover_blue(image_remove_blue)

image_recover_blue_no_contrast = image_operation.recover_blue_no_contrast(image_remove_blue)
# image_operation.compare_image(ori_image, image_remove_blue)
mse_blue = image_operation.compare_image(ori_image, image_recover_blue)
mse_blue_no_contrast = image_operation.compare_image(ori_image, image_recover_blue_no_contrast)

# %%
# gamma transform
ori_image = image_operation.gamma2_transform(ori_image)

image_remove_red = image_operation.gamma2_transform(image_remove_red)
image_recover_red = image_operation.gamma2_transform(image_recover_red)
image_recover_red_no_contrast = image_operation.gamma2_transform(image_recover_red_no_contrast)

image_remove_green = image_operation.gamma2_transform(image_remove_green)
image_recover_green = image_operation.gamma2_transform(image_recover_green)
image_recover_green_no_contrast = image_operation.gamma2_transform(image_recover_green_no_contrast)

image_remove_blue = image_operation.gamma2_transform(image_remove_blue)
image_recover_blue = image_operation.gamma2_transform(image_recover_blue)
image_recover_blue_no_contrast = image_operation.gamma2_transform(image_recover_blue_no_contrast)
# %%
fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(18, 10))

# plot ori_image
axes[0, 0].imshow(ori_image)
axes[0, 0].set_title('Original image')
axes[0, 0].set_xticks([])
axes[0, 0].set_yticks([])
axes[0, 0].spines['top'].set_visible(False)
axes[0, 0].spines['right'].set_visible(False)
axes[0, 0].spines['bottom'].set_visible(False)
axes[0, 0].spines['left'].set_visible(False)
# plot image_remove_red
axes[0, 1].imshow(image_remove_red)
axes[0, 1].set_title('Image remove red')
axes[0, 1].set_xticks([])
axes[0, 1].set_yticks([])
axes[0, 1].spines['top'].set_visible(False)
axes[0, 1].spines['right'].set_visible(False)
axes[0, 1].spines['bottom'].set_visible(False)
axes[0, 1].spines['left'].set_visible(False)
# plot image_recover_red
axes[0, 2].imshow(image_recover_red)
axes[0, 2].set_title('Image recover red (MSE = {:.2f})'.format(mse_red))
axes[0, 2].set_xticks([])
axes[0, 2].set_yticks([])
axes[0, 2].spines['top'].set_visible(False)
axes[0, 2].spines['right'].set_visible(False)
axes[0, 2].spines['bottom'].set_visible(False)
axes[0, 2].spines['left'].set_visible(False)
# plot image_recover_red_no_contrast
axes[0, 3].imshow(image_recover_red_no_contrast)
axes[0, 3].set_title('Image recover red (no contrast) (MSE = {:.2f})'.format(mse_red_no_contrast))
axes[0, 3].set_xticks([])
axes[0, 3].set_yticks([])
axes[0, 3].spines['top'].set_visible(False)
axes[0, 3].spines['right'].set_visible(False)
axes[0, 3].spines['bottom'].set_visible(False)
axes[0, 3].spines['left'].set_visible(False)

# plot ori_image
axes[1, 0].imshow(ori_image)
axes[1, 0].set_title('Original image')
axes[1, 0].set_xticks([])
axes[1, 0].set_yticks([])
axes[1, 0].spines['top'].set_visible(False)
axes[1, 0].spines['right'].set_visible(False)
axes[1, 0].spines['bottom'].set_visible(False)
axes[1, 0].spines['left'].set_visible(False)
# plot image_remove_green
axes[1, 1].imshow(image_remove_green)
axes[1, 1].set_title('Image remove green')
axes[1, 1].set_xticks([])
axes[1, 1].set_yticks([])
axes[1, 1].spines['top'].set_visible(False)
axes[1, 1].spines['right'].set_visible(False)
axes[1, 1].spines['bottom'].set_visible(False)
axes[1, 1].spines['left'].set_visible(False)
# plot image_recover_green
axes[1, 2].imshow(image_recover_green)
axes[1, 2].set_title('Image recover green (MSE = {:.2f})'.format(mse_green))
axes[1, 2].set_xticks([])
axes[1, 2].set_yticks([])
axes[1, 2].spines['top'].set_visible(False)
axes[1, 2].spines['right'].set_visible(False)
axes[1, 2].spines['bottom'].set_visible(False)
axes[1, 2].spines['left'].set_visible(False)
# plot image_recover_green_no_contrast
axes[1, 3].imshow(image_recover_green_no_contrast)
axes[1, 3].set_title('Image recover green (no contrast) (MSE = {:.2f})'.format(mse_green_no_contrast))
axes[1, 3].set_xticks([])
axes[1, 3].set_yticks([])
axes[1, 3].spines['top'].set_visible(False)
axes[1, 3].spines['right'].set_visible(False)
axes[1, 3].spines['bottom'].set_visible(False)
axes[1, 3].spines['left'].set_visible(False)

# plot ori_image
axes[2, 0].imshow(ori_image)
axes[2, 0].set_title('Original image')
axes[2, 0].set_xticks([])
axes[2, 0].set_yticks([])
axes[2, 0].spines['top'].set_visible(False)
axes[2, 0].spines['right'].set_visible(False)
axes[2, 0].spines['bottom'].set_visible(False)
axes[2, 0].spines['left'].set_visible(False)
# plot image_remove_blue
axes[2, 1].imshow(image_remove_blue)
axes[2, 1].set_title('Image remove blue')
axes[2, 1].set_xticks([])
axes[2, 1].set_yticks([])
axes[2, 1].spines['top'].set_visible(False)
axes[2, 1].spines['right'].set_visible(False)
axes[2, 1].spines['bottom'].set_visible(False)
axes[2, 1].spines['left'].set_visible(False)
# plot image_recover_green
axes[2, 2].imshow(image_recover_blue)
axes[2, 2].set_title('Image recover blue (MSE = {:.2f})'.format(mse_blue))
axes[2, 2].set_xticks([])
axes[2, 2].set_yticks([])
axes[2, 2].spines['top'].set_visible(False)
axes[2, 2].spines['right'].set_visible(False)
axes[2, 2].spines['bottom'].set_visible(False)
axes[2, 2].spines['left'].set_visible(False)
# plot image_recover_blue_no_contrast
axes[2, 3].imshow(image_recover_blue_no_contrast)
axes[2, 3].set_title('Image recover blue (no contrast) (MSE = {:.2f})'.format(mse_blue_no_contrast))
axes[2, 3].set_xticks([])
axes[2, 3].set_yticks([])
axes[2, 3].spines['top'].set_visible(False)
axes[2, 3].spines['right'].set_visible(False)
axes[2, 3].spines['bottom'].set_visible(False)
axes[2, 3].spines['left'].set_visible(False)

fig.tight_layout()

plt.savefig(image_name[:-4] + '_recover.jpg', dpi=300)

plt.show()
