#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:05:51 2020

@author: robinvonbargen
"""
import random

import TrainingData
import NearestNeighbors
import UserInterface


# ------------------ Help functions for cluster generation ------------------
def create_data_cluster(number_of_data_points, x_start, x_end, y_start, y_end, label = "?"):
    data_cluster_list = []
    for i in range(number_of_data_points + 1):
        data_point = TrainingData.TrainingData()
        feature_vector = [random.randrange(x_start, x_end), random.randrange(y_start, y_end)]
        data_point.set_feature_vector(feature_vector)
        data_point.set_label(label)
        data_cluster_list.append(data_point)
    return data_cluster_list
        
def remove_duplicates(list_of_datapoints):
    stripped_list = []
    [stripped_list.append(data_point) for data_point in list_of_datapoints if not data_point in stripped_list]
    return stripped_list

# ---------------------------------------------------------------------------
    


def main():
    training_data = []
    test_data = []
    
    # Cluster sizes
    cluster_one_size = 6
    cluster_two_size = 15
    cluster_three_size = 12
    
    # Cluster intervals
    cluster_one_interval = [-10, -5, -10, -5]
    cluster_two_interval = [0, 3, -2, 4]
    cluster_three_interval = [2, 6, 8, 10]
    
    # Cluster labels
    cluster_one_label = "a"
    cluster_two_label = "b"
    cluster_three_label = "c"
    
    # Create random clusters
    cluster_one = remove_duplicates(create_data_cluster(
            cluster_one_size,
            cluster_one_interval[0],
            cluster_one_interval[1],
            cluster_one_interval[2],
            cluster_one_interval[3],
            cluster_one_label
    ))
    cluster_two = remove_duplicates(create_data_cluster(
            cluster_two_size,
            cluster_two_interval[0],
            cluster_two_interval[1],
            cluster_two_interval[2],
            cluster_two_interval[3],
            cluster_two_label
    ))
    cluster_three = remove_duplicates(create_data_cluster(
            cluster_three_size,
            cluster_three_interval[0],
            cluster_three_interval[1],
            cluster_three_interval[2],
            cluster_three_interval[3],
            cluster_three_label
    ))
    
    # Add clusters to training data
    training_data = [*cluster_one, *cluster_two, *cluster_three]
    
    # Create test data
    number_of_test_points = 5
    test_data_interval = [
            min(
                [
                    cluster_one_interval[0], 
                    cluster_two_interval[0], 
                    cluster_three_interval[0]
                ]
            ),
            max(
                [
                    cluster_one_interval[1], 
                    cluster_two_interval[1], 
                    cluster_three_interval[1]
                ]
            ),
            min(
                [
                    cluster_one_interval[2], 
                    cluster_two_interval[2], 
                    cluster_three_interval[2]
                ]
            ),
            max(
                [
                    cluster_one_interval[3], 
                    cluster_two_interval[3], 
                    cluster_three_interval[3]
                ]
            )
        ]
    
    test_data = remove_duplicates(create_data_cluster(
            number_of_test_points,
            test_data_interval[0],
            test_data_interval[1],
            test_data_interval[2],
            test_data_interval[3]
    ))
    
    # Init the kNN - algorithm and classify data
    k = 3
    knn = NearestNeighbors.NearestNeighbors(training_data)
    classified_data = knn.classify_data(test_data, k)
    
    
    # Plot unclassified data
    ui = UserInterface.UserInterface()
    ui.load_training_data(training_data)
    ui.load_test_data(test_data)
    ui.update()
    ui.draw_plot(scale_axis = False)
    
    # Plot classified data
    ui = UserInterface.UserInterface()
    ui.load_training_data(training_data)
    ui.load_test_data(classified_data)
    ui.update()
    ui.draw_plot(scale_axis = False)
    
     
main()

