print (__doc__)

import numpy as np
import pylab as pl
from sklearn import svm

#create 40 randoms sperable points
np.random.seed(0)
x = np.r_[np.random.randn(20,2)-[2,2], np.random.randn(20,2)+[2,2]]
y = [0] * 20 + [1] * 20

#fit model
clf = svm.SVC(kernel='linear')
clf.fit(x,y)

#get the eparating hyper plane
w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(-5,5)
yy = a * xx - (clf.intercept_[0])/w[1]

b = clf.support_vectors_[0]
yy_down = a * xx + (b[1] - a * b[0])
b = clf.support_vectors_[-1]
yy_up = a * xx + (b[1]-a * b[0])

print "w: ", w
print "a: ", a

print "support vector :", clf.support_vectors_
print "clf.coef_:", clf.coef_

print "predict: ", clf.predict([[-3,6],[-3,5],[-3,4],[3,1],[3,2],[3,3]])

pl.plot(xx,yy,'b-')
pl.plot(xx,yy_down,'k--')
pl.plot(xx,yy_up,'k--')
pl.scatter(clf.support_vectors_[:,0], clf.support_vectors_[:,1],
           s = 88, facecolor = 'none')
pl.scatter(x[:,0],x[:,1],c=y,cmap=pl.cm.Paired)
pl.axis('tight')
pl.show()







