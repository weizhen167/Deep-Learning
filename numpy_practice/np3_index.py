import numpy as np

a = np.arange(3,15)
print 'a is: '
print a

b = a[3]
print 'b is: '
print b

a = np.arange(3,15).reshape((3,4))
print 'new_a is: '
print a

c = a[2][1]
c = a[2,1]
print 'c is: '
print c


# all numbers of row 2
d = a[2,:]
# all numbers of col 1
d_1 = a[:,1]
# row 1 && col 1:3
d_2 = a[1,1:3]
print 'd is: '
print d
print 'd_1 is: '
print d_1
print 'd_2 is: '
print d_2



print
print '----------part2---------- \n\n'

print '\nreturn all the rows in a'
for row in a:
    print row

print '\nreturn all the columns in a'
for column in a.T:
    print column


e = a.flatten()
print 'e is: '
print e


print '\nreturn all the item in a'
#use flat!!!!!
for item in a.flat:
    print item

print
print '----------part3---------- \n\n'
#append array

a = np.array([1,1,1])
b = np.array([2,2,2])

print 'a is: '
print a

print 'b is: '
print b


# vertical stack
c = np.vstack((a,b))
print '\nc is: '
print c

#horizontal stack
d = np.hstack((a,b))
print '\nd is: '
print d

# wwant to make  array from _ to |
# T not works
e = a.T
print '\ne is: '
print e

e_new1 = a[np.newaxis,:]
e_new2 = a[:,np.newaxis]
print '\ne_new is: '
print e_new1
print e_new2

f1 = a[:,np.newaxis]
f2 = b[:,np.newaxis]
f = np.hstack((f1,f2))
print '\nf is: '
print f


g = np.concatenate((f1,f2,f1),axis=1)
print '\ng is: '
print g

print
print '----------part4---------- \n\n'
#cut array


a = np.arange(12).reshape(3,4)
print '\na is: '
print a

# split only use as even split
b = np.split(a,2,axis=1)
print '\nb is: '
print b

# uneven split
c = np.array_split(a,3,axis=1)
print '\nc is: '
print c


d = np.vsplit(a,3)
print '\nd is: '
print d

e = np.hsplit(a,2)
print '\ne is: '
print e

