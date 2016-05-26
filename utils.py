# -*- coding: utf-8 -*-
"""
Created on Mon May 23 21:17:02 2016

@author: zhaoming
"""
import time
import math

class TestResultGen(object):
    """
    input 2 list, double, sort by time then district id
    """
    @staticmethod
    def get_test_result(predict, target):
        if len(predict) != len(target):
            return -1

        sum = 0.0
        for in range(len(predict)):
            sum += abs(target[i] - predict[i]/target[i])

        return sum/len(predict)


class Util(object):
    def get_time_slot(time_string):
        t = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
        ret_str = time.strftime("%Y-%m-%d", t) + "-"
        ret_str += str(int(math.floor((t.hour * 24 + t.minute)/10) + 1))

        return ret_str







