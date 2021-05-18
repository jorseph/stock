# -*- coding: utf-8 -*-
"""
Created on Tue May 18 23:46:15 2021

@author: jorseph
"""
class DataGenerator:
    def __init__(self, stock_code):
        self.stock_code = stock_code
        self.df = self.create_features()
    
    def create_features(self):
        

