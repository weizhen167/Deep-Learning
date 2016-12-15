import numpy as np

x = np.array([[0,0],[0,1],[1,0],[1,1]])
x = np.atleast_2d(x)
temp = np.ones([x.shape[0], x.shape[1] + 1])
temp[:, 0:-1] = x
x = temp
i = np.random.randint(x.shape[0])

# tanh activation method
def tanh(x):
    return np.tanh(x)
# tanh activation method
def tanh_deriv(x):
    return 1.0 - np.tanh(x)*np.tanh(x)

print (tanh([ 347861.33218041 ,332873.21665686 ,341182.53269112]))