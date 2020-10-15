#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:11:20 2020

@author: robinvonbargen
"""

class TrainingDataTable:
    def __init__(self):
        self.__table = []
    
    def get_table(self):
        return self.__table
    
    def add_element(self, training_data):
        self.__table.append(training_data)