#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 13:55:31 2019

@author: hp
"""

from sklearn.metrics.pairwise import cosine_similarity

class cosine:
    def calculateCosineSimilarity(self, firstList, secondList):
        print("Calculating cosine values")
        trueCosineValues = []
        cosineTable = cosine_similarity(firstList,secondList)
        for i in range (0, len(firstList)):
            if(cosineTable[i][i] > 0.3):
                trueCosineValues.append(1)
            else:
                trueCosineValues.append(0)
        return trueCosineValues
            
    def calculateTrueValues(self,dataSet):
        return dataSet.iloc[:,5].values
