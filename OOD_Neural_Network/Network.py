import Connections, Layer,Connection

class Network(object):
    def __init__(self, layers):
        '''
        init a full coeection NN
        layers: 2d array, discribe how many nodes in each layer
        '''
        self.connections = Connections()
        self.layers = []
        layer_count = len(layers)
        node_count = 0;
        for i in range(layer_count):
            self.layers.append(Layer(i, layers[i]))
        for layer in range(layer_count - 1):
            connections = [Connection(upstream_node, downstream_node)
                           for upstream_node in self.layers[layer].nodes
                           for downstream_node in self.layers[layer + 1].nodes[:-1]]
            for conn in connections:
                self.connections.add_connection(conn)
                conn.downstream_node.append_upstream_connection(conn)
                conn.upstream_node.append_downstream_connection(conn)




    def train(self, labels, data_set, rate, iteration):
        '''
        train NN
        labels: array,train sample tags. each element is a sample tag.
        data_set: 2d array,features of train sample. each element is a feature.
        '''
        for i in range(iteration):
            for d in range(len(data_set)):
                self.train_one_sample(labels[d], data_set[d], rate)




    def train_one_sample(self, label, sample, rate):
        '''
        interinal, run one time
        '''
        self.predict(sample)
        self.calc_delta(label)
        self.update_weight(rate)




    def calc_delta(self, label):
        '''
        internal, calcuelate delta of each node.
        '''
        output_nodes = self.layers[-1].nodes
        for i in range(len(label)):
            output_nodes[i].calc_output_layer_delta(label[i])
        for layer in self.layers[-2::-1]:
            for node in layer.nodes:
                node.calc_hidden_layer_delta()





    def update_weight(self, rate):
        '''
        internal function, update W of each connection
        '''
        for layer in self.layers[:-1]:
            for node in layer.nodes:
                for conn in node.downstream:
                    conn.update_weight(rate)




    def calc_gradient(self):
        '''
        internal function, calcuelate gradient of each connection
        '''
        for layer in self.layers[:-1]:
            for node in layer.nodes:
                for conn in node.downstream:
                    conn.calc_gradient()




    def get_gradient(self, label, sample):
        '''
        under a NN sample, calc gradient of each connection
        label: sample lable
        sample: sample input
        '''
        self.predict(sample)
        self.calc_delta(label)
        self.calc_gradient()


    def predict(self, sample):
        '''
        predict
        sample: arrrary,features,
        '''
        self.layers[0].set_output(sample)
        for i in range(1, len(self.layers)):
            self.layers[i].calc_output()
        return map(lambda node: node.output, self.layers[-1].nodes[:-1])

    def dump(self):
        for layer in self.layers:
            layer.dump()