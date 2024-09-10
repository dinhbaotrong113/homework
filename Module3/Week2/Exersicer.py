import pandas as pd
import numpy as np
import csv
import math 
# KNN WITH EUCLIDEAN DISTANCE
# read dataset and set datatrain vs datatest
file = open('D:/Homework/Module3/Week2/Iris.csv', 'r')
data = csv.reader(file)
data = np.array(list(data))

data = np.delete(data, 0, 0)
data = np.delete(data, 0, 1)

file.close()
trainingset = data[:49]
testingset = data[49:]

# function caculator Euclidean distance computation

def computeDistance(dataPoint1, Datapoint2):
    result = 0
    for i in range(4):
        result += (float(dataPoint1[i])-float(Datapoint2[i]))**2
    return math.sqrt(result)

# function compute and return KNN

def computeKnearestneighbor(trainingSet, item, k):
    distance = []
    for datapoint in trainingSet:
        distance.append({
            'Label': datapoint[-1],
            'Value': computeDistance(datapoint, item)
        })
    distance.sort(key = lambda x: x['Value'])
    label = [x['Label'] for x in distance]
    return label[:k]
# voting the distance to fined the predictted result

def voteTheDistances(array):
    labels = set(array)
    kmax = 0
    result = ''
    for i in labels:
        k = array.count(i)
        if k > kmax:
            kmax = k
            result = i
    return i

# testing

k = 3
for i in testingset:
    array = computeKnearestneighbor(trainingset, i, k)
    result = voteTheDistances(array)
    print("GT: ", i[-1], ', Perediction: ', result)

# KNN WITH COSINE SIMILITY DISTANCE