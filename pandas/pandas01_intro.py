import pandas as pd
import numpy as np


s = pd.Series([1,3,6,np.nan,44,1])
print s
print '\n'

dates = pd.date_range('20170101',periods=6)
print dates
print '\n'

df = pd.DataFrame(np.random.randn(6,4),index=dates, columns=['a','b','c','d'])
print df
print '\n'

df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print df1
print '\n'

df2 = pd.DataFrame({'A':1,
                    'B':pd.Timestamp('20170101'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4, dtype='int32'),
                    'E':pd.Categorical(['test','train','test','train']),
                    'F':'foo'})

#
print '----------------------------'
print '\n'
print df2


print '\n+++dtypes: '
print df2.dtypes

print '\n+++index: '
print df2.index

print '\n+++columns:'
print df2.columns

print '\n+++values:'
print df2.values

print '\n+++describe:'
print df2.describe


print '\n+++TTT:'
print df2
print '\n'
print df2.T


#sort index
print '\n\n----------------------------sort index---------------------------- '
print df2
print '\n1:\n'
print df2.sort_index(axis=1,ascending=False)
print '\n2:\n'
print df2.sort_index(axis=0,ascending=False)
#sort values

print '\nsort by value: '
print df2.sort_values(by='E')
