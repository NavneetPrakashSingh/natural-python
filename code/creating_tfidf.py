#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:35:48 2019

@author: hp
"""
from sklearn.feature_extraction.text import CountVectorizer
class creatingTFIDF:
    def create(self, corpus):
        cv = CountVectorizer(max_features=1500) #reducing sparcity
        X = cv.fit_transform(corpus).toarray()
        return X

    def createDependentVariable(self,dataset):
        return dataset.iloc[:,6].values