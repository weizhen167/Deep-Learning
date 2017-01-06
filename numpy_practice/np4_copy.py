import numpy as np

a = np.arange(3,15)
print 'a is: '
print a

b = a
print 'b is: '
print b

c = a
print 'c is: '
print c

d = b
print 'd is: '
print d

print '\n____________________________ change start_________________'


print 'now a[0] = 11'
a[0] = 11
print 'a is: '
print a
print 'b is: '
print b
print 'c is: '
print c
print 'd is: '
print d


print '\n\nnow d[1:3] = 22,33'
d[1:3] = [22,33]
print 'a is: '
print a
print 'b is: '
print b
print 'c is: '
print c
print 'd is: '
print d


print '\n\n----------test1----------'
a = np.arange(3,15)
print 'a is: '
print a
b = a.copy()  #deep copy
print 'b is: '
print b

print '\nnow a[0] = 11'
a[0] = 11
print 'a is: '
print a
print 'b is: '
print b





