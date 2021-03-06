#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 18:29:27 2020

@author: haoqiwang
"""

from lib import image_operation

from matplotlib import pyplot as plt

IMAGE_FOLDER = './image_database/'
image_name = 'natural_forest.jpg'

image_path = IMAGE_FOLDER + image_name

# %%
# remove and recover red
ori_image = image_operation.read_image(image_path)
image_remove_red = image_operation.remove_red(ori_image)
image_recover_red = image_operation.recover_red(image_remove_red)

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

# plot ori_image
axes[0].imshow(ori_image)
axes[0].set_title('Original image')
axes[0].set_xticks([])
axes[0].set_yticks([])
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)
axes[0].spines['bottom'].set_visible(False)
axes[0].spines['left'].set_visible(False)
# plot image_remove_red
axes[1].imshow(image_remove_red)
axes[1].set_title('Image remove red')
axes[1].set_xticks([])
axes[1].set_yticks([])
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)
axes[1].spines['bottom'].set_visible(False)
axes[1].spines['left'].set_visible(False)
# plot image_recover_red
axes[2].imshow(image_recover_red)
axes[2].set_title('Image recover red')
axes[2].set_xticks([])
axes[2].set_yticks([])
axes[2].spines['top'].set_visible(False)
axes[2].spines['right'].set_visible(False)
axes[2].spines['bottom'].set_visible(False)
axes[2].spines['left'].set_visible(False)

fig.tight_layout()

# plt.savefig("natural_forest_image_recover_red",dpi=300)

plt.show()
# %%
# remove and recover green
ori_image = image_operation.read_image(image_path)
image_remove_green = image_operation.remove_green(ori_image)
image_recover_green = image_operation.recover_green(image_remove_green)

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

# plot ori_image
axes[0].imshow(ori_image)
axes[0].set_title('Original image')
axes[0].set_xticks([])
axes[0].set_yticks([])
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)
axes[0].spines['bottom'].set_visible(False)
axes[0].spines['left'].set_visible(False)
# plot image_remove_green
axes[1].imshow(image_remove_green)
axes[1].set_title('Image remove green')
axes[1].set_xticks([])
axes[1].set_yticks([])
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)
axes[1].spines['bottom'].set_visible(False)
axes[1].spines['left'].set_visible(False)
# plot image_recover_green
axes[2].imshow(image_recover_green)
axes[2].set_title('Image recover green')
axes[2].set_xticks([])
axes[2].set_yticks([])
axes[2].spines['top'].set_visible(False)
axes[2].spines['right'].set_visible(False)
axes[2].spines['bottom'].set_visible(False)
axes[2].spines['left'].set_visible(False)

fig.tight_layout()

# plt.savefig("natural_forest_image_recover_green",dpi=300)

plt.show()
# %%
# remove and recover blue
ori_image = image_operation.read_image(image_path)
image_remove_blue = image_operation.remove_blue(ori_image)
image_recover_blue = image_operation.recover_blue(image_remove_blue)

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

# plot ori_image
axes[0].imshow(ori_image)
axes[0].set_title('Original image')
axes[0].set_xticks([])
axes[0].set_yticks([])
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)
axes[0].spines['bottom'].set_visible(False)
axes[0].spines['left'].set_visible(False)
# plot image_remove_blue
axes[1].imshow(image_remove_blue)
axes[1].set_title('Image remove blue')
axes[1].set_xticks([])
axes[1].set_yticks([])
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)
axes[1].spines['bottom'].set_visible(False)
axes[1].spines['left'].set_visible(False)
# plot image_recover_green
axes[2].imshow(image_recover_blue)
axes[2].set_title('Image recover blue')
axes[2].set_xticks([])
axes[2].set_yticks([])
axes[2].spines['top'].set_visible(False)
axes[2].spines['right'].set_visible(False)
axes[2].spines['bottom'].set_visible(False)
axes[2].spines['left'].set_visible(False)

fig.tight_layout()

# plt.savefig("natural_forest_image_recover_blue",dpi=300)

plt.show()
# %%
# combine all together
ori_image = image_operation.read_image(image_path)
image_remove_red = image_operation.remove_red(ori_image)
image_recover_red = image_operation.recover_red(image_remove_red)

ori_image = image_operation.read_image(image_path)
image_remove_green = image_operation.remove_green(ori_image)
image_recover_green = image_operation.recover_green(image_remove_green)

ori_image = image_operation.read_image(image_path)
image_remove_blue = image_operation.remove_blue(ori_image)
image_recover_blue = image_operation.recover_blue(image_remove_blue)

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 12))

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
axes[0, 2].set_title('Image recover red')
axes[0, 2].set_xticks([])
axes[0, 2].set_yticks([])
axes[0, 2].spines['top'].set_visible(False)
axes[0, 2].spines['right'].set_visible(False)
axes[0, 2].spines['bottom'].set_visible(False)
axes[0, 2].spines['left'].set_visible(False)

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
axes[1, 2].set_title('Image recover green')
axes[1, 2].set_xticks([])
axes[1, 2].set_yticks([])
axes[1, 2].spines['top'].set_visible(False)
axes[1, 2].spines['right'].set_visible(False)
axes[1, 2].spines['bottom'].set_visible(False)
axes[1, 2].spines['left'].set_visible(False)

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
axes[2, 2].set_title('Image recover blue')
axes[2, 2].set_xticks([])
axes[2, 2].set_yticks([])
axes[2, 2].spines['top'].set_visible(False)
axes[2, 2].spines['right'].set_visible(False)
axes[2, 2].spines['bottom'].set_visible(False)
axes[2, 2].spines['left'].set_visible(False)

fig.tight_layout()

plt.savefig("natural_forest_image_recover", dpi=300)

plt.show()
