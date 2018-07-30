'''
Created on 2018-07-30

@author: steven
'''

import cv2
from cv2 import imread

print(cv2)
print (imread)
from matplotlib import pyplot as plt 

import os

folder = os.path.dirname(__file__)+os.path.sep
print ('folder: ', folder)



# must add folder as prefix
# img = imread(folder + 'messi.jpg', 0)
img = imread(folder + '01.jpg', 0)

print('img: ', img)

# plt.imshow(None, cmap='gray', interpolation='bicubic')
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.show()

