#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:10:24 2020

@author: robinvonbargen
"""

class TrainingData:
    def __init__(self):
        self.__feature_vector = None
        self.__label = None
    
    def get_feature_vector(self):
        return self.__feature_vector
    
    def set_feature_vector(self, feature_vector):
        self.__feature_vector = feature_vector
    
    def get_label(self):
        return self.__label
    
    def set_label(self, label):
        self.__label = label
    
    def copy(self):
        new_object = TrainingData()
        new_object.set_label(self.get_label())
        new_object.set_feature_vector(self.get_feature_vector().copy())
        return new_object

