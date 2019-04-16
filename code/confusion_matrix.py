#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:20:23 2019

@author: hp
"""
from sklearn.metrics import confusion_matrix
class confusionMatrix:
    def createConfusionMatrix(self,calculatedValues,predictedValues):
        return confusion_matrix(calculatedValues,predictedValues)