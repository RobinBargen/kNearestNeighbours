#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 21:27:41 2020

@author: robinvonbargen
"""

import matplotlib.pyplot as plt

class ColorSelector:
    def __init__(self, number_of_labels):
        self.__number_of_labels = number_of_labels
        self.__cmap = plt.cm.get_cmap('hsv', self.__number_of_labels)
    
    def get_color(self, label_index):
        return self.__cmap(label_index)