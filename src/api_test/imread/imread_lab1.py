'''
Created on 2018-08-01

@author: steven
'''

from cv2 import imread, split, merge
import os
from os.path import sep
from ipdb import set_trace
import matplotlib.pyplot as plt

file = os.path.dirname(__file__)+ sep + '..' + sep + 'img' + sep + '01.jpg'
print('file path: ', file)

img = imread(file)
b, g, r = split(img)

img_rgb = merge([r, g, b])

def show_raw2(img, cmap=None):
    set_trace()
    plt.imshow(img, cmap=cmap, interpolation='bicubic')
    plt.show() 


