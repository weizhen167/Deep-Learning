import numpy as np

a = np.array([10,20,30,40])
b = np.arange(4)

print 'a is: ', a
print 'b is: ', b
print

c = a-b
print 'c is: ', c

d = a+b
print 'd is: ', d

e = a*b
print 'e is: ', e

f = b**2
print 'f is: ', f

g = 10*np.sin(a)
print 'g is: ', g

h = 10*np.cos(a)
print 'h is: ', h

j = (b<3)
#print 'j is: ', j

print
print '----------2d matrix operation----------'
i = np.array([[1,1],
              [0,1]])
print 'i is: '
print i

j = b.reshape((2,2))
print 'j is: '
print j

# multiply and dot multiply
k = i*j

k_dot =np.dot(i,j)
k_dot2 = i.dot(j)
print 'k is: '
print k
print 'k_dot is: '
print k_dot


l = np.random.random((2,4))
print 'l is: '
print l
# row
np.sum(l,axis = 1)
# column
np.min(l,axis = 0)
# general
np.max(l)

print
print '----------2d matrix operation 2----------'

a = np.arange(2,14).reshape((3,4))
print 'a is: '
print a

# all of these value can be calculate as row or column
b = np.argmin((a))
print 'b is: '
print b

b_1 = np.argmax((a))
print 'b_1 is: '
print b_1

b_2 = np.mean((a),axis = 0)
b_2= a.mean()
print 'b_2 is: '
print b_2

b_3 = np.median((a))
print 'b_3 is: '
print b_3

c = np.cumsum(a)
print 'c is: '
print c

#lei cha
d =np.diff(a)
print 'd is: '
print d

#return 2 list of all the none zero elements' x,y
e  = np.nonzero(a)
print 'e is: '
print e



print
print '----------2d matrix operation 3----------'
a = np.arange(14,2,-1).reshape((3,4))
print 'new a is: '
print a

#transpose
f = np.transpose(a)
f_1 = (a.T)
print 'f is: '
print f
print 'f_1 is: '
print f_1

#clip
#if value < 5, make it = 5
#if value >9 make it = 9
g = np.clip(a,5,9)
print 'g is: '
print g

