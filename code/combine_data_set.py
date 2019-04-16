#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:27:19 2019

@author: hp
"""

class combineDataSet:
    def combineDataSet(self, dataset):
        combinedDataSet = []
        for i in range(0,len(dataset)):
            combinedDataSet.append(dataset["question1"][i]+" "+dataset["question2"][i])
        return combinedDataSet;