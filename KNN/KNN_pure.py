import csv
import random
import math
import operator
from sklearn import datasets

def loadDataset(filename,split,trainingSet=[],testSet=[]):
    with open (filename, 'rb') as cdvfile:
        lines = csv.reader(cdvfile)
        dataset=list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
                if random.random() < split:
                    trainingSet.append(dataset[x])

def euclideanDistance(instance1,instance2,length):
    distance = 0
    for x in range (length):
        distance += pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)

def getNeighbors(trainingset, testinstance,k):
        distance = []
        length = len(testinstance)
        for x in range (len(trainingset)):
            dist = euclideanDistance(testinstance,trainingset[x],length)
            distance.append(trainingset[x],dist)
        distance.sort(key=operator.itemgetter(1))
        neighbors = []
        for i in range(k):
            neighbors.append(distance[x][0])
        return neighbors

def getresponse(neighbors):
    classvotes = {}
    for x in range(len(neighbors)):
        reposnse= neighbors[x][-1]
        if reposnse in classvotes:
            classvotes[reposnse]+=1
        else:
            classvotes[reposnse] = 1
    sortdvotes = sorted(classvotes.iteritems(),key=operator.itemgetter(1),reverse = True)

def getaccuracy(testset,predictions):
    correct  = 0
    for x in range(len(testset)):
        if testset[x][-1] == predictions[x]:
            correct += 1
    print str(testset)
    return (correct/float(len(testset)))*100.0

def main():
    trainingset=[]
    testset=[0.3,0.4,0.3,0.4]
    split= 0.67
    loadDataset("iris.txt",split,trainingset,testset)
    print "train set: " + repr(len(trainingset))
    print "test set: "+ repr(len(testset))

    predictions = []
    k = 3
    for x in range(len(testset)):
        neighbors = getNeighbors(trainingset,testset[x],k)
        result = getresponse(neighbors)
        predictions.append(result)
        print "> predicted=" + repr(result) + ", actual=" + repr(testset[x][-1])
    accuracy = getaccuracy(testset,predictions)
    print('accurancy: ' + repr(accuracy)  +"%")

main()