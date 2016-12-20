import numpy as np


# tanh activation method
def tanh(x):
    return np.tanh(x)
# tanh activation method
def tanh_deriv(x):
    return 1.0 - np.tanh(x)*np.tanh(x)

# logistic method
def logistic(x):
    return 1/(1+np.exp(-x))

# logistic_derivative method
def logistic_derivative(x):
    return logistic(x)*(1-logistic(x))


class NeuralNetwork:

    def __init__(self, layers, activation = 'tanh'):
        # layers is a list that contains how many units in each layer.
        # for example: [5,2,2]
        # means first layer 5 units, second layer 2 units, third layer 2 units
        #print str(layers)
        if(activation == 'logistic'):
            self.activation = logistic
            self.activation_deriv=logistic_derivative
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tanh_deriv

        #init the weights, give all of the start weights a random value.
        self.weights = []
        for i in range(1,len(layers)-1):
            self.weights.append((2*np.random.random((layers[i-1]+1, layers[i] + 1))-1)*0.25)
            self.weights.append((2*np.random.random((layers[i] + 1, layers[i + 1]))-1)*0.25)
        #print str(self.weights)


    def fit(self,x,y,learning_rate=0.2,epochs=10000):
        x = np.atleast_2d(x)
        temp = np.ones([x.shape[0],x.shape[1]+1])
        temp[:,0:-1] = x
        x=temp
        #print str(x)
        y=np.array(y)
        for k in range(epochs):
            #print "**************" + str(k) + "**************"
            i = np.random.randint(x.shape[0])
            a=[x[i]]

            for l in range(len(self.weights)):
                a.append(self.activation(np.dot(a[l],self.weights[l])))
            error = y[i] - a[-1]
            deltas = [error*self.activation_deriv(a[-1])]
            for l in range(len(a)-2,0,-1):
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_deriv(a[l]))
            deltas.reverse()
            for i in range(len(self.weights)):
                layer = np.atleast_2d((a[i]))
                delta = np.atleast_2d(deltas[i])
                self.weights[i] += learning_rate * layer.T.dot(delta)

    def predict(self,x):
        x = np.array(x)
        temp = np.ones(x.shape[0]+1)
        temp[0:-1]=x
        a=temp
        for l in range(0,len(self.weights)):
            a=self.activation(np.dot(a,self.weights[l]))
        return a

if __name__ == '__main__':
    nn = NeuralNetwork([2, 2, 1], 'tanh')
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])
    nn.fit(x, y)
    for i in [[0, 0], [0, 1], [1, 0], [1, 1]]:
        ss = str(nn.predict(i))
        print i, ss
        if (ss < 0.5):
            pass
            # print (i,"0")

        else:
            pass
            # print (i,"1")

