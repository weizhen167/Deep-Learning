import numpy as np

array = np.array([[1,2,3],
                  [2,3,4]])

print array

print 'number of dim:', array.ndim
print "shape:", array.shape
print 'size', array.size


print '----------------section 2----------------'
# no ',' between elements
# dtype many types: int float
a = np.array([2,3,4],dtype=np.float)
print a.dtype

#2d array
b = array = np.array([[1, 2, 3],
                      [2, 3, 4]])

# init  x*y matrix with 0
c = np.zeros((3,4))
print c

# init  x*y matrix with 1
d = np.ones((3,4))
print d

#init  x*y matrix with empty
e = np.empty((3,4))
print e

#make a array, from 10 to 20, step is 2
f = np.arange(10,20,2)
print f

#make a matrix with a range of number
g = np.arange(12).reshape((3,4))
print g

#make a line space, from 1 to 10, should include 20 lines
h = np.linspace(1,10,20).reshape((5,4))
print h








