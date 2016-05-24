#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
description
1. load data from train set, save as numpy array
2. passenger data predict
"""

class DataProvider(object):
    FEATURE_NUM = 10
    SAMPLE_NUM = 144 * (FEATURE_NUM + 1)

    def __init__(self, data_path):
        self.order_data_path = './data/order/'
        self.poi_data_pat = './data/poi/'

    def load_feature_xxx():
        pass

    def save_req_feature_data():
        pass

    def save_answer_feature_data():
        pass


class Model(object):
    def __int__(self, dataprovider):
        self.data_provider = dataprovider
        self.target_data_path = './data/'

    def get_predict_data():
        pass

    def get_test_cost():
        pass

    def get_submit_data():
        pass

