# -*- coding: utf-8 -*-
"""
Created on Mon May 23 21:17:02 2016

@author: zhaoming
"""
import datetime
import math
import csv
import numpy as np

class TestResultGen(object):
    """
    input 2 list, double, sort by time then district id
    """
    @staticmethod
    def get_test_result(predict, target):
        if len(predict) != len(target):
            return -1

        sum = 0.0
        for i in range(len(predict)):
            sum += abs(target[i] - predict[i]/target[i])

        return sum/len(predict)


class Util(object):
    BASE_DATETIME = datetime.datetime.strptime('2016-01-01', '%Y-%m-%d')
    @staticmethod
    def get_time_slot(timeObj):
        t = timeObj
        ret_str = t.strftime("%Y-%m-%d") + '-'
        ret_str += str(int(math.floor((t.hour * 60 + t.minute)/10) + 1))
        time_slot = int(math.floor((t.hour * 60 + t.minute)/10) + 1)
        time_diff = int(math.floor(((t - Util.BASE_DATETIME).total_seconds())/(60*10)))
        return time_diff, time_slot

        #return ret_str
    @staticmethod
    def batch_read(filename, batch=50):
        with open(filename, 'rb') as data_stream:
            batch_output = list()
            for n,row in enumerate(csv.reader(data_stream, dialect='excel')):
                if n > 0 and n % batch ==0:
                    yield (np.array(batch_output))
                batch_output.append(row)
            yield(np.array(batch_output))







