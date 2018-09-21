'''
Created on 2018-09-04

@author: steven
'''

import os

class LoriManager(object):
    def __init__(self):
        pass
    def set_home_path(self, path):
        self.home_path = path
    def get_home_path(self):
        return self.home_path
    def get_home_pics(self, path):
        home_pic_list = os.listdir(self.home_path)
        return home_pic_list
    
    
    
        

