#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:43:12 2019

@author: hp
"""
import pandas as pd;

#importing the data set happens in this file
class loading_file:
    def loading(self, CSVFilePath):
        dataSet = pd.read_csv(CSVFilePath, dtype={3:'str', 4:'str'})
        return dataSet