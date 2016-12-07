from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree


data_file = "mylearn.csv"

with open(data_file,"r") as f:
    reader=csv.reader(f)
    header=reader.next()
    print header

    feature_list=[]
    label_list=[]

    for row in reader:
        label_list.append(row[len(row)-1])
        rowDict={}
        for i in range(1,len(row)-1):
            rowDict[header[i]]=row[i]
        feature_list.append(rowDict)
    print(feature_list)

vec = DictVectorizer()
dummyX=vec.fit_transform(feature_list).toarray()
print "dummyX: \n" + str(dummyX)
print vec.get_feature_names()
print "liablelist: " + str(label_list)

lb=preprocessing.LabelBinarizer()
dummyY =lb.fit_transform(label_list)
print"dummyY: \n" + str(dummyY)

clf=tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(dummyX,dummyY)
print('clf: ' + str(clf))

with open("sample.dot", "w") as f:

    f = tree.export_graphviz(clf,feature_names=vec.get_feature_names(),out_file=f)

oneRowX= dummyX[0,:]
print('oneRowX; ' + str(oneRowX))

newRowX = oneRowX

newRowX[0] = 1
newRowX[2] = 0
print('oneRowX; ' + str(newRowX))

predictedY = clf.predict(newRowX)
print "predictedY: " + str(predictedY)