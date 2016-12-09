from sklearn import svm

x=[[2,0],[1,1],[2,3]]
y= [0,0,1]

clf = svm.SVC(kernel= 'linear')
clf.fit(x,y)



# print classfiyer
print clf


#print support vectors
print clf.support_vectors_
#which spot of the input data were support vectors?
print clf.support_
#how many support vectors were found from each data group?
print clf.n_support_

# predict a new point and class where it belongs to
print clf.predict([[2,1],[3,3]])