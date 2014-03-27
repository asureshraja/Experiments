from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
inLayer = LinearLayer(1)
hiddenLayer = SigmoidLayer(2)
outLayer = LinearLayer(1)
n = FeedForwardNetwork()
n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)
in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)
#in_to_out = FullConnection(inLayer, outLayer)
#n.addConnection(in_to_out)
n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)
n.sortModules()
print (n)
data = SupervisedDataSet(1,1)
data.addSample([1/97],[1/1])
data.addSample([1/98],[1/2])
data.addSample([1/99],[1/3])
data.addSample([1/100],[1/4])
t = BackpropTrainer(n, data, learningrate = 0.01, momentum = 0.99, verbose = True)
for epoch in range(0,1000):
	t.train()
print(n.activate([1/97]))
print(n.activate([1/98]))
print(n.activate([1/99]))
print(n.activate([1/100]))
print(n.activate([1/113]))