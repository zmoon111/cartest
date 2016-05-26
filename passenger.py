#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
description
1. load data from train set, save as numpy array
2. passenger data predict
"""

import numpy as np
import matplotlib.pyplot as plt
from utils import Util


class DataProvider(object):
    FEATURE_LIST = ['timeslot', 'weather', 'poi', 'traffic']
    MATRIX_NUM = 21 * 144 * (len(FEATURE_LSIT) + 1)

    def __init__(self, data_path='training_data/'):
        self.order_data_path = './data_path/order/'
        self.poi_data_path = './data_path/poi/'

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



