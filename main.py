# print("Hello world")

# from utilities import read_image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np

I = mpimg.imread('natural_forest.jpg')

print(I.shape)
plt.imshow(I)
