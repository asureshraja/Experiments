import pickle
import sahelper as lib
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer,TanhLayer,SoftmaxLayer,GaussianLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
lib.initiate()
inLayer = LinearLayer(390)
hiddenLayer = SigmoidLayer(75)
outLayer = LinearLayer(1)
n =FeedForwardNetwork()

n.addInputModule(inLayer)
n.addModule(hiddenLayer)
n.addOutputModule(outLayer)
in_to_hidden = FullConnection(inLayer, hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer, outLayer)
n.addConnection(in_to_hidden)
n.addConnection(hidden_to_out)

n.sortModules()
data = SupervisedDataSet(390,1)
data.addSample(lib.generate("anitha"),0)

t = BackpropTrainer(n, data, learningrate = 0.1, momentum = 0.10, verbose = True)

for epoch in range(0,1000):
    t.train()
print "raja",n.activate(lib.generate("raja"))

f = open('tmp_pickle.pic', 'wb')
pickle.dump(n, f)
f.close()
#
#f = open('tmp_pickle.pic', 'rb')
#i = pickle.load(f)
#f.close()