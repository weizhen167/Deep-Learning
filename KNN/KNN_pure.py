import csv
import random
import math
import operator
from sklearn import datasets  #import files

#create data set, feed in a data file,
# create a training set and a test set.
#file name: input file path
#split: how many % of file will go to the
# training Set and how many go to test set.
#the lias line of data is the class name

def loadDataset(filename,split,trainingSet=[],testSet=[]):
    with open (filename, 'rb') as cdvfile:
        lines = csv.reader(cdvfile)# csvreader
        dataset =list(lines) #init dataset
        for x in range(len(dataset)-1):
            for y in range(4):
                # read csv file and keep the values as float
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:  #if less than split value, go to training set
                trainingSet.append(dataset[x])
            else:          #else go to test set
                testSet.append(dataset[x])


#caluate the distance between the given instances
#instance is a list, first 4 elements are valid values,
# and the last element is the class of this set of value
#for example : [7.7,3.8,6.7,2.2,Iris-virginica]
#length ：how long is the valid value of the instance
def euclideanDistance(instance1,instance2,length):
    distance = 0
    for x in range(length):
        # keep adding the (instance1[x]-instance2[x])^2
        distance += pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance) #return the distance of these two instance




#get k Neighbors from training set,
# based on the distance between test instance
# and every entry of the training set
def getNeighbors(trainingset, testinstance,k):
        distance = []
        length = len(testinstance)-1
        for x in range (len(trainingset)):
            dist = euclideanDistance(testinstance,trainingset[x],length)
            distance.append((trainingset[x],dist))
        distance.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(k):
            neighbors.append(distance[x][0])
        return neighbors


#return the closest neighbor for a list of neighbors
def getresponse(neighbors):
    classvotes = {}
    for x in range(len(neighbors)):
        reposnse= neighbors[x][-1]
        if reposnse in classvotes:
            classvotes[reposnse]+=1
        else:
            classvotes[reposnse] = 1
    sortdvotes = sorted(classvotes.iteritems(),
                        key=operator.itemgetter(1),reverse = True)
    return sortdvotes[0][0]



#Statistical accuracy of our predictions
#walk through all the entry of testset and
# count how many % of the predictions are correct
def getaccuracy (testset,predictions):
    correct = 0
    for x in range(len(testset)):
        if testset[x][-1] == predictions[x]:
            correct += 1

    return (correct/float(len(testset)))*100.0



#main method
def main():
    trainingset=[]
    testset=[]
    split= 0.67
    loadDataset("iris.txt",split,trainingset,testset)
    print "train set: " + repr(len(trainingset))
    print "test set: " + repr(len(testset))

    predictions = []
    k = 3
    for x in range(len(testset)):
        neighbors = getNeighbors(trainingset,testset[x],k)
        result = getresponse(neighbors)
        predictions.append(result)
        print "> predicted=" + repr(result) + ", actual=" +\
              repr(testset[x][-1])
    accuracy = getaccuracy(testset,predictions)
    print('accurancy: ' + repr(accuracy)  +"%")




#run
main()