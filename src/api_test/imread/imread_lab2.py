'''
Created on 2018-08-02

@author: steven
'''

from cv2 import imread, split
import os
from os.path import sep

import matplotlib.pyplot as plt

# file = os.path.dirname(__file__)+os.path.sep + '01.jpg'
file = os.path.dirname(__file__)+ sep + '..' + sep + 'img' + sep + '01.jpg'

img = imread(file)

b, g, r = split(img)

figure = plt.figure()
figure.subplots_adjust(hspace=0.3)

pic1 = figure.add_subplot(221)
pic1.imshow(b)
pic1.set_title('b channel')

pic2 = figure.add_subplot(222)
pic2.imshow(r)
pic2.set_title('r channel')

pic3 = figure.add_subplot(223)
pic3.imshow(g)
pic3.set_title('g channel')

plt.show()

