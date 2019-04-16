#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:43:47 2019

@author: hp
"""
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB

class machineLearning:
    def machineLearningAlgorithm(self,createSetTFIDF, trueOutcomes):
        print("Calculating machine learning values")
        #split into training and test data
        X_train, X_test, Y_train, Y_test = train_test_split(createSetTFIDF,trueOutcomes,test_size=0.1,random_state=0)
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.fit_transform(X_test)   
        
        classifier = GaussianNB()
        classifier.fit(X_train,Y_train)
        
        y_predict = classifier.predict(X_test)
        
        return [y_predict,Y_test]
        