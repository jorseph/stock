# -*- coding: utf-8 -*-
"""
Created on Tue May 18 23:46:15 2021

@author: jorse
"""
class DataGenerator:
    def __init__(self, company_code, data_path='./stock_history', output_path='./outputs', strategy_type='original',
                 update=False, logger: Logger = None):
        self.company_code = company_code
        self.df = self.create_features()
