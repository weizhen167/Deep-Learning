import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods = 6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])


print df


print '\n\n'
print df['A'],df.A


print '\n\n'
print df[0:3],df['20130102':'20130104']

print '\n\n'

#select by label: loc
print df.loc['20130102']
print df.loc[:,['A','B']]
print df.loc['20130102',['A','B']]

#select by position: iloc
print df.iloc[3:5,1:3]

#mixed selection ix
print df.ix[:3,['A','C']]

#boolean indexing
print df[df.A>8]


print '---------------------value setting----------------------'
df.iloc[2,2] = 1111
df.loc['20130101','B'] = 2222
df[df.A>4] = 0
df['F'] = np.nan
df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))
print df


print '---------------------deal with nan data----------------------'
dates = pd.date_range('20130101',periods = 6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
print df

#print df.dropna()

##print df.dropna(axis=0,how='any') #how = {'any','all'}
##print df.fillna(value = 0)

print df.isnull()
print np.any(df.isnull())== True