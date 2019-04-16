#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:08:06 2019

@author: hp
"""
import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


#cleaning the data set
class cleaningDataSet:
    def clean(self, dataSet,colName):
        corpus_sentences = []
        for i in range(len(dataSet)):
            #removing non alphabets
            newDataSet = re.sub('[^a-zA-Z]',' ',str(dataSet[colName][i]))
            
            #turning it into lower case
            newDataSet = newDataSet.lower()
            
            #removing stopwords
            newDataSet = newDataSet.split()
            ps = PorterStemmer()
            newDataSet = [ps.stem(words) for words in newDataSet if not words in set(stopwords.words('english'))]
            newDataSet = ' '.join(newDataSet)
            
            #stemming words
            corpus_sentences.append(newDataSet)

        return corpus_sentences
    
    def cleanList(self,dataSet):
        corpus_sentences = []
        for i in range(len(dataSet)):
            #removing non alphabets
            newDataSet = re.sub('[^a-zA-Z]',' ',dataSet[i])
            
            #turning it into lower case
            newDataSet = newDataSet.lower()
            
            #removing stopwords
            newDataSet = newDataSet.split()
            ps = PorterStemmer()
            newDataSet = [ps.stem(words) for words in newDataSet if not words in set(stopwords.words('english'))]
            newDataSet = ' '.join(newDataSet)
            
            #stemming words
            corpus_sentences.append(newDataSet)

        return corpus_sentences
         
    
        