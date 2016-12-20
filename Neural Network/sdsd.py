import numpy as np


# tanh activation method
def tanh(x):
    return np.tanh(x)
# tanh activation method
def tanh_deriv(x):
    return np.tanh(x)*(1.0 - np.tanh(x))

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
        print len(layers)-1
        for i in range(1,len(layers)-1):
            print '&&&&&&&&&&&&&&&&&&&&&&&&&'+str(i)+'&&&&&&&&&&&&&&&&&&&&&&&&&'
            print (layers[i-1]+1, layers[i] + 1  )
            print (layers[i]  +1, layers[i  + 1] )
            #print np.random.random((layers[i-1]+1, layers[i] + 1))
            #print '[][][]['
            #print 2 * np.random.random((layers[i - 1] + 1, layers[i] + 1))


            self.weights.append((2*np.random.random((layers[i-1]+1, layers[i] + 1)) - 1)*0.25)
            self.weights.append((2*np.random.random((layers[i] + 1, layers[i + 1] ) ) - 1)*0.25)
        print str(self.weights)


    def fit(self,x,y,learning_rate=0.2,epochs=10000):
        x = np.atleast_2d(x)
        temp = np.ones([x.shape[0],x.shape[1]+1])
        temp[:,0:-1] = x
        x=temp
        print str(x)
        y=np.array(y)
        for k in range(epochs):
            print "**************" + str(k) + "**************"
            i = np.random.randint(x.shape[0])
            #print str("random number\n" + str(i))
            a=[x[i]]
            #print str("choose a random row of the input\n" + str(a))

            for l in range(len(self.weights)):
                #print str("----------------------------------8\n" + str(a))
                print l
                print str(a[l])
                print str(self.weights[l])
                #print str("np.dot(a[l],self.weights[l]) 8.5\n" + str(np.dot(a[l], self.weights[l])))
                #print str("np activation")
                a.append(self.activation(np.dot(a[l],self.weights[l])))

                #print str("append all of the values after activation 8.5\n" + str(a))
            error = y[i] - a[-1]
            #print str(y[i]) + "-" + str(a[-1])
           # print str("-------------------error is-------9\n" + str(error))
            deltas = [error*self.activation_deriv(a[-1])]
            #print str("----------------------------------10\n" + str(deltas))

            #print str("----------------------------------11\n" + str(range(len(a)-2,0,-1)))
            for l in range(len(a)-2,0,-1):
                deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_deriv(a[l]))
             #   print str("----------------------------------12\n" + str(deltas))
            deltas.reverse()
            #print str("----------------------------------13\n" + str(deltas))
            #print str("----------------------------------14\n" + str(len(self.weights)))
            for i in range(len(self.weights)):
                layer = np.atleast_2d((a[i]))
             #   print str("----------------------------------15\n" + str(layer))
                delta = np.atleast_2d(deltas[i])
             #   print str("----------------------------------16\n" + str(layer))
                self.weights[i] += learning_rate * layer.T.dot(delta)

    def predict(self,x):
        #print self.weights
        x = np.array(x)
        #print "----------------------------------\n"+str(x)
        temp = np.ones(x.shape[0]+1)
        temp[0:-1]=x
        a=temp
        #print str(a)
        for l in range(len(self.weights)):
            #print str((a,self.weights[l])) + "wowowowowow"
            #print str(np.dot(a,self.weights[l])) +"hohohohohohoho"
            a=self.activation(np.dot(a,self.weights[l]))
            #print str(a) + "HAHAHAHAHAHA"
        return a

if __name__ == '__main__':
    nn = NeuralNetwork([2,2,1],'tanh')
    x = np.array([[0,0],[0,1],[1,0],[1,1]])
    y = np.array([1,0,0,1])
    nn.fit(x,y)
    #print nn.weights
    #print "len of weight " + str(len(nn.weights))
    for i in [[0,0],[0,1],[1,0],[1,1]]:
        ss = str(nn.predict(i))
        print i, ss
        if(ss < 0.5):
            pass
            #print (i,"0")

        else:
            pass
            #print (i,"1")

