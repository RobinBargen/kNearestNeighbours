#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:03:54 2020

@author: robinvonbargen
"""
import math

class DataPointDistance:
    def __init__(self):
        pass
    
    def get_distance(self, data_point_start, data_point_end):
        squared_distance = 0
        for i in range(len(data_point_start.get_feature_vector())):
            squared_distance += (data_point_end.get_feature_vector()[i] - data_point_start.get_feature_vector()[i])**(2)
        return math.sqrt(squared_distance)

