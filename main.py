# print("Hello world")

# from utilities import read_image

#from utilities import remove_color

'''
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import numpy as np

I = mpimg.imread('natural_forest.jpg')
I=np.asarray(I).astype(np.int32)
#print(I.shape)
plt.imshow(I)
plt.imshow(I,cmap="gray")
#plt.colorbar()
#remove red
I2=I[:,:,0]
plt.imshow(I2,cmap="gray")
'''
from utilities import remove_color
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

filename='natural_forest.jpg'
ori_image = mpimg.imread(filename)
image = np.asarray(ori_image).astype(np.int32)
plt.imshow(image)
image_remove_red = remove_color.remove_red(image)
#image_remove_green=remove_color.remove_green(image)
plt.show()
