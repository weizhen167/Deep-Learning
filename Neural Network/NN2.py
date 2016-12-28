class Perceptron(object):
    def __init__(self, input_num, activator):
        '''
        actvation function double -> double
        '''
        self.activator = activator
        # w = 0
        self.weights = [0.0 for _ in range(input_num)]
        # b = 0
        self.bias = 0.0


    def __str__(self):
        '''
        print W, b
        '''
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)


    def predict(self, input_vec):
        #print input_vec
        s1 = zip(input_vec, self.weights)
        #print 's1' + str(s1)
        a1 = map(lambda (x, w): x * w,s1)
        #print 'a1' +  str(a1)
        '''
        input victor , output result
        '''
        # pack X and W together
        # change to [(x1,w1),(x2,w2),(x3,w3),...]
        # use map to calculate:[x1*w1, x2*w2, x3*w3]
        # use reduce get SUM
        s = self.activator(
            reduce(lambda a, b: a + b,a1, 0.0) + self.bias
        )
        return s


    def train(self, input_vecs, labels, iteration, rate):
        '''
        training data: a group of vector and corresponding label;training round, learning rate
        '''
        for i in range(iteration):
            self._one_iteration(input_vecs, labels, rate)


    def _one_iteration(self, input_vecs, labels, rate):
        '''
        one, iteration, train all the datas
        '''
        # pach input and oupput become sample list: [(input_vec, label), ...]
        # each training sample is : (input_vec, label)
        samples = zip(input_vecs, labels)

        # for each sample, update W based on the NN rules
        for (input_vec, label) in samples:
            # calculate the output based on current W
            output = self.predict(input_vec)
            # update w
            self._update_weights(input_vec, output, label, rate)



    def _update_weights(self, input_vec, output, label, rate):
        '''
        update w
        '''
        # pach input_vec[x1,x2,x3,...] and weights[w1,w2,w3,...] together
        # become[(x1,w1),(x2,w2),(x3,w3),...]
        # update w based on NN rules
        delta = label - output
        #print 'delta: ' + str(delta)
        a1 = zip(input_vec, self.weights)
        #print 'a1: ' + str(a1)
        self.weights = map(lambda (x, w): w + rate * delta * x,a1)
        #print 'self.weights: ' + str(self.weights)
        # update bias
        self.bias += rate * delta
        #print 'self.basis' + str(self.bias)
        #print '\n'

def f(x):
    '''
    define activaction function
    '''
    return 1 if x > 0 else 0



def get_training_dataset():
    # build train set
    # input list
    input_vecs = [[1,1], [0,0], [1,0], [0,1]]
    # expect output list, must correspond of each input list
    # [1,1] -> 1, [0,0] -> 0, [1,0] -> 0, [0,1] -> 0
    labels = [1, 0, 0, 0]
    return input_vecs, labels

def train_and_perceptron():
    # training NN, input parmater as '2' (and is a 2 parmater function), activation is f
    p = Perceptron(2, f)
    # train 10 rounds, learning rate is 0.1
    input_vecs, labels = get_training_dataset()
    p.train(input_vecs, labels, 100, 0.1)
    #return trained NN
    return p


if __name__ == '__main__':
    and_perception = train_and_perceptron()
    #print and_perception
    print '\n\n\n\n'
    print '1 and 1 = %d' % and_perception.predict([1, 1])
    print '0 and 0 = %d' % and_perception.predict([0, 0])
    print '1 and 0 = %d' % and_perception.predict([1, 0])
    print '0 and 1 = %d' % and_perception.predict([0, 1])