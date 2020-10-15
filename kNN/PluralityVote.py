#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 19:08:43 2020

@author: robinvonbargen
"""

class PluralityVote:
    def __init__(self):
        self.__labels = []
        self.__votes = []
        

    def __load_labels(self, data_point_list):
        for data_point in data_point_list:
            if(data_point.get_label() not in self.__labels):
                self.__labels.append(data_point.get_label())
                
                
    def __count_votes(self, data_point_list):
        self.__votes = [0 for _ in range(len(self.__labels))]
        for data_point in data_point_list:
            self.__votes[self.__labels.index(data_point.get_label())] += 1

    def __get_leading_label(self):
        return self.__labels[self.__votes.index(max(self.__votes))]

    def get_plurality_vote(self, data_point_list):
        self.__load_labels(data_point_list)
        self.__count_votes(data_point_list)
        print("---- Plurality vote results: ----")
        print(self.__labels)
        print(self.__votes)
        print(self.__get_leading_label())
        return self.__get_leading_label()
