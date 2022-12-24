#!/usr/bin/python3
import sys
from os import listdir
import numpy as np
import operator

def createDataSet(dirname):
	labels = []
	trainingList = listdir(dirname)
	mlen = len(trainingList)
	matrix = np.zeros((mlen, 1024))

	for i in range(mlen):
		fileNameStr = trainingList[i]
		answer = int(fileNameStr.split('_')[0])
		labels.append(answer)
		matrix[i, :] = gVector(dirname + '/' + fileNameStr)
	return matrix, labels 

def classify0(inX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat ** 2
	sqDistances = sqDiffMat.sum(axis = 1)
	distances = sqDistances ** 0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}

	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		if voteIlabel not in classCount.keys():
			classCount[voteIlabel] = 0
		classCount[voteIlabel] += 1
		sortedClassCount = sorted(classCount.items(), key= operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

def gVector(fName):
	returnVector = np.zeros((1, 1024))
	with open(fName) as file:
		for i in range(32):
			line = file.readline()
			for j in range(32):
				returnVector[0, 32 * i + j] = int(line[j])
		return returnVector        

trainingDirName = sys.argv[1]
testDirName = sys.argv[2]

testList = listdir(testDirName)
testLen = len(testList)

matrix, labels = createDataSet(trainingDirName)

for k in range(1, 21):
	cnt = 0 
	errorCnt = 0
    
	for i in range(testLen):
		answer = int(testList[i].split('_')[0])
		testData = gVector(testDirName + '/' + testList[i])
		classifiedResult = classify0(testData, matrix, labels, k)
        
		cnt += 1
		if answer != classifiedResult :
			errorCnt += 1
	errorPer = errorCnt / cnt * 100
	print(int(errorPer))

