#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 11:41:17 2019

@author: hp
"""
from loading_file import *
from cleaning_data_set import *
from creating_tfidf import *
from cosine import *
from confusion_matrix import *
from combine_data_set import *
from machine_learning import *

CSVFilePath = "./dataset.csv"
#CSVFilePath = "./train.csv"
loadingFiles = loading_file()
dataSet = loadingFiles.loading(CSVFilePath)
dataSet.info()
clean_column_one_sentences = []
clean_column_two_sentences = []

cleaningFile = cleaningDataSet()
clean_column_one_sentences = cleaningFile.clean(dataSet,'question1')
clean_column_two_sentences = cleaningFile.clean(dataSet,'question2')

createTFIDF = creatingTFIDF()
first_column_TFIDF = createTFIDF.create(clean_column_one_sentences)
second_column_TFIDF = createTFIDF.create(clean_column_two_sentences)

#--------------- Cosine Similarity ------------------------------------#

cosineSimilarity = cosine()
predictedOutcome = cosineSimilarity.calculateCosineSimilarity(first_column_TFIDF,second_column_TFIDF)
trueOutcomes = cosineSimilarity.calculateTrueValues(dataSet)

confusionMatrixObj = confusionMatrix()
confusionMatrixValues = confusionMatrixObj.createConfusionMatrix(predictedOutcome,trueOutcomes)
print("Accuracy using cosine is: ",(confusionMatrixValues[0][0]+confusionMatrixValues[1][1])/10,"%")
precisionCos = confusionMatrixValues[1][1]/(confusionMatrixValues[1][1]+confusionMatrixValues[1][0])
recallCos = confusionMatrixValues[1][1]/(confusionMatrixValues[1][1]+confusionMatrixValues[0][1])
fmeasureCos = (2 * precisionCos * recallCos)/(precisionCos + recallCos)
print("Precision: ", precisionCos)
print("Recall: ", recallCos)
print("F-measure: ", fmeasureCos)

#-------------- Machine Learning -------------------#

combinedDataSetQuestionColumn = combineDataSet()
questionSet = combinedDataSetQuestionColumn.combineDataSet(dataSet)

cleanDataSet = cleaningFile.cleanList(questionSet)

createTFIDF = createTFIDF.create(cleanDataSet)

machineLearningObj = machineLearning()
returningValues = machineLearningObj.machineLearningAlgorithm(createTFIDF,trueOutcomes)

confusionMatrixValuesUsingML = confusionMatrixObj.createConfusionMatrix(returningValues[1],returningValues[0])
print("Accuracy using Naive Bayes algorithm is: ",(confusionMatrixValuesUsingML[0][0]+confusionMatrixValuesUsingML[1][1])/1 ,"%")
precisionML = confusionMatrixValuesUsingML[1][1]/(confusionMatrixValuesUsingML[1][1]+confusionMatrixValuesUsingML[1][0])
recallML = confusionMatrixValuesUsingML[1][1]/(confusionMatrixValuesUsingML[1][1]+confusionMatrixValuesUsingML[0][1])
fmeasureML = (2 * precisionML * recallML)/(precisionML + recallML)
print("Precision: ", precisionML)
print("Recall: ", recallML)
print("F-measure: ", fmeasureML)





