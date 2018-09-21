'''
Created on 2018-07-30

@author: steven
'''

import cv2
from cv2 import imread
from pdb import set_trace

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

class MSLab(object):
    def __init(self):
        pass
        
    def lab1(self):
        global img
        img += 1
        print('img2: ', img)
    


lab = MSLab()
lab.lab1()

# plt.imshow(None, cmap='gray', interpolation='bicubic')
def show():
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.show()
    
def show_raw(img, cmap=None):
    set_trace()
    plt.imshow(img, cmap=cmap, interpolation='bicubic')
    plt.show() 

show()

