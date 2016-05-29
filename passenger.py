#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
description
1. load data from train set, save as numpy array
2. passenger data predict in model
"""


import csv
import os
import sys
import random
import argparse
import datetime
import collection

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from utils import Util


class DataProvider(object):
    FEATURE_LIST = ['index', 'weekofday','daytimeindex','weather', 'poi', 'traffic']
    MATRIX_ROWS = 21 * 144
    MATRIX_COLS = (len(FEATURE_LIST) + 1)  #21 days data + 1 col target value
    ORDER_TABLE_DESC = ['order_id', 'driver_id', 'passenger_id', 'start_district_has', 'dest_district_hash', 'price', 'time']
    

    def __init__(self, data_path='season_1'):
        self.order_data_path = data_path + '/training_data/order_data/'
        self.poi_data_path = data_path + '/training_data/poi_data/'
        self.weather_data_path = data_path + '/training_data/weather_data/'
        self.traffic_data_path = data_path + '/training_data/traffic_data/'
        self.id_mapping = data_path + '/training_data/cluster_map/'
        
        self._feature_matrix = np.zeros((self.MATRIX_ROWS, self.MATRIX_COLS), dtype='float', order='C')
        
        self.batch_size = 1000
        lst = os.listdir(self.order_data_path)
        
        lst = os.listdir(self.order_data_path)
        for orderfile in lst:
            orders_chunk = pd.read_csv(self.order_data_path + orderfile, sep='\t', decimal='.', header=None, names=self.ORDER_TABLE_DESC,
                                 parse_dates=[len(self.ORDER_TABLE_DESC)-1], error_bad_lines=False, chunksize=self.batch_size)
            for orders in orders_chunk:
                for i in range(0, self.batch_size-1):
                    row_index, time_index = Util.get_time_slot((orders['time'][i]).to_datetime())
                    self._feature_matrix[row_index][0] = row_index
                    self._feature_matrix[row_index][1] = (orders['time'][i]).to_datetime().date().weekday() + 1
                    self._feature_matrix[row_index][2] = time_index
                    self._feature_matrix[row_index][len(self.FEATURE_LIST)] += 1
                    print self._feature_matrix[row_index]
                    
                
    def save():
        self._feature_matrix

    def load_feature_xxx(self):
        day_index = 0
        time_slot_index = 0
        pass

    def save_req_feature_data(self):
        pass



class Model(object):
    def __int__(self, dataprovider):
        self.data_provider = dataprovider
        self.target_data_path = './data/'

    def get_predict_data(self):
        pass

    def get_test_cost(self):
        pass

    def get_submit_data(self):
        pass



