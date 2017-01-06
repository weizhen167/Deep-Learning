import pandas as pd
import numpy as np

#read_XXXXXXXX
data = pd.read_csv('student.csv', sep='\t')
print data

#to_XXXXXXXXXXSSSS
data.to_pickle('student.pickle')

print '\n\n\n----------------------pandas append --------------------'

# concatenation

df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'],index=[1,2,3])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'],index=[1,2,3])

print df1
print df2
print df3

res = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
#print res

#join, ['inner','outer']

df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'],index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['b','c','d','e'],index=[2,3,4])

res1 = pd.concat([df1,df2])
print res1

res2 = pd.concat([df1,df2],join='outer',ignore_index=True)
print res2
res2 = pd.concat([df1,df2],join='inner')
print res2

# join axes
res3 = pd.concat([df1,df2],axis = 1,join_axes=[df1.index])
print res3

# append
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1,columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2,columns=['a','b','c','d'])
res4 = df1.append([df2,df3],ignore_index=True)
print res4

print '\n\n'
df1 = pd.DataFrame(np.ones((3,4))*0,columns=['a','b','c','d'])
s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
res5 = df1.append(s1,ignore_index=True)
print res5

print '\n\n\n----------------------pandas merge --------------------'

#merging two df by key/keys (may be used in data base)


#simple example

print '--------simple example------------'
left = pd.DataFrame({'key':['K0','K1','K2','K3'],
                     'A':['A0','A1','A2','A3'],
                     'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'C': ['C0', 'C1', 'C2', 'C3'],
                     'D': ['D0', 'D1', 'D2', 'D3']})

print left
print right

res = pd.merge(left,right,on='key')
print '\n'
print res


# consider two keys
print '\n--------two keys------------\n'
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print left
print right
#how = ['left','right','inner','outer']
res = pd.merge(left,right,on=['key1','key2'],how = 'right')
res1 = pd.merge(left,right,on=['key1','key2'],how = 'left')
res2 = pd.merge(left,right,on=['key1','key2'],how = 'inner')
res3 = pd.merge(left,right,on=['key1','key2'],how = 'outer')
print '\n'
print res
print '\n'
print res1
print '\n'
print res2
print '\n'
print res3



#give the indicator a custom name
df1 = pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print df1
print df2
res = pd.merge(df1,df2,on='col1',how='outer',indicator=True)
res = pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_col')
print res


#---------------------- merge_index------------------
#merged by index
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index= ['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                      'D': ['D0', 'D1', 'D2']},
                     index = ['K0', 'K1', 'K2'])

print left
print right

res = pd.merge(left,right,left_index=True,right_index=True,how='outer')
print res



#handing overlapping

boys = pd.DataFrame({'k':['K0', 'K1', 'K2'],'age':[1,2,3]})
girls = pd.DataFrame({'k':['K0', 'K0', 'K3'],'age':[4,5,6]})

print '\n\n\n\n'
print boys
print girls

res = pd.merge(boys,girls,on='k',suffixes=['_boy','_girl'],how='inner')
print res