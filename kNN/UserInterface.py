#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:12:24 2020

@author: robinvonbargen
"""

import matplotlib.pyplot as plt

import ColorSelector


class UserInterface:
    def __init__(self):
        self.__figure_name = 'knn_demo.png'
        self.__training_data = None
        self.__test_data = None
        self.__color_selector = None
        self.__data_labels = None
        
    
    def load_training_data(self, training_data):
        self.__training_data = training_data.copy()
    
    
    def load_test_data(self, learning_data):
        self.__test_data = learning_data.copy()
        
    
    def __update_labels(self):
        data_labels = []
        for data_point in [*self.__training_data, *self.__test_data]:
            point_label = data_point.get_label()
            if(point_label not in data_labels):
                data_labels.append(point_label)
        self.__data_labels = data_labels
        
    
    def __update_color_selector(self, number_of_labels):
        self.__color_selector = ColorSelector.ColorSelector(number_of_labels)
    
    
    def update(self):
        self.__update_labels()
        self.__update_color_selector(len(self.__data_labels))
    
    
    def draw_plot(self, scale_axis = True):
        if(self.__training_data is None):
            return
        
        fig = plt.figure()
        if(not scale_axis):
            plt.gca().set_aspect('equal', adjustable='box')
        for data_point in self.__training_data:
            point_features = data_point.get_feature_vector()
            point_label = data_point.get_label()
            
            label_index = self.__data_labels.index(point_label)
            
            plt.annotate(point_label, (point_features[0], point_features[1]))
            plt.scatter(point_features[0], point_features[1], c = self.__color_selector.get_color(label_index))
        
        for data_point in self.__test_data:
            point_features = data_point.get_feature_vector()
            point_label = data_point.get_label()
            
            label_index = self.__data_labels.index(point_label)
            
            plt.annotate(point_label, (point_features[0], point_features[1]))
            plt.scatter(point_features[0], point_features[1], c = self.__color_selector.get_color(label_index))
        
        fig.show()
    
    