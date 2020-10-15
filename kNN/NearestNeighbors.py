#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:07:23 2020

@author: robinvonbargen
"""
import TrainingDataTable
import DataPointDistance
import PluralityVote

class NearestNeighbors:
    def __init__(self, training_data):
        self.__training_data_table = self.__init_data_table(training_data.copy())
        
    def __init_data_table(self, training_data):
        training_data_table = TrainingDataTable.TrainingDataTable()
        for element in training_data:
            training_data_table.add_element(element.copy())
        return training_data_table
    
    
    def __calculate_distances(self, test_data_point, training_data):
        distance_list = []
        for i in range(len(training_data)):
            training_data_point = training_data[i]
            distance = DataPointDistance.DataPointDistance().get_distance(test_data_point, training_data_point)
            distance_list.append(distance)
        return distance_list


    def __get_nearest_neighbors(self, test_data_point, training_data, neighborhood_size):
        # Calculate distances to all neighboring points
        distances = self.__calculate_distances(test_data_point, training_data)

        # Load the neigborhood
        neighborhood = []
        neighbors_found = 0
        candidates = training_data.copy()
        while(neighbors_found < neighborhood_size):
            closest_neighboring_index = distances.index(min(distances))
            neighbour = candidates.pop(closest_neighboring_index)
            distances.pop(closest_neighboring_index)
            neighborhood.append(neighbour)
            neighbors_found += 1
        return neighborhood

                    
    def classify_data(self, test_data, neighborhood_size):
        test_data_table = self.__init_data_table(test_data.copy())
        classified_test_data = []
        for test_data_point in test_data_table.get_table():
            nearest_neighbors = self.__get_nearest_neighbors(
                    test_data_point, 
                    self.__training_data_table.get_table(), 
                    neighborhood_size
            )
            classification_label = PluralityVote.PluralityVote().get_plurality_vote(nearest_neighbors)
            test_data_point.set_label(classification_label)
            classified_test_data.append(test_data_point)
        return classified_test_data

