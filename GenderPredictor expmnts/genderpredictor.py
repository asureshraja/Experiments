import pickle
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer,TanhLayer,SoftmaxLayer,GaussianLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
lib.initiate()
inLayer = LinearLayer(260)
hiddenLayer = SigmoidLayer(7)
outLayer = LinearLayer(10)
n =FeedForwardNetwork()

n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)
in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)
n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)

n.sortModules()
data = SupervisedDataSet(10,10)
data.addSample(lib.generate("anitha"),lib.generate("f"))

t = BackpropTrainer(n, data, learningrate = 0.1, momentum = 0, verbose = True)

for epoch in range(0,1000):
    t.train()
print "giridhar",lib.reverse(n.activate(lib.generate("giridhar")))

f = open('tmp_pickle.pic', 'wb')
pickle.dump(n, f)
f.close()
#
#f = open('tmp_pickle.pic', 'rb')
#i = pickle.load(f)
#f.close()