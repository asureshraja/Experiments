import numpy
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer,TanhLayer,SoftmaxLayer,GaussianLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
inLayer = LinearLayer(2)
hiddenLayer = SigmoidLayer(3)
outLayer = LinearLayer(1)
n =FeedForwardNetwork()

n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)
in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)
n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)
new_params = numpy.array([1.0]*13)
in_to_hidden._setParameters(new_params)
print in_to_hidden.params
n.sortModules()
data = SupervisedDataSet(2,1)
data.addSample([1,1],[0])
data.addSample([1,0],[1])
data.addSample([0,1],[1])
data.addSample([0,0],[0])
t = BackpropTrainer(n, data, learningrate = 0.1, momentum = 0.99, verbose = True)
for epoch in range(0,1000):
    t.train()
print(n.activate([1,1]))
print(n.activate([1,0]))
print(n.activate([0,1]))
print(n.activate([0,0]))
