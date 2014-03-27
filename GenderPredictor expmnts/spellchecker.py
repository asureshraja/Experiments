import pickle
import precalcspellchecker as lib
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer,TanhLayer,SoftmaxLayer,GaussianLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
lib.initiate()
inLayer = LinearLayer(10)
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
data.addSample(lib.generate("kousalya"),lib.generate("f"))
data.addSample(lib.generate("dhivya"),lib.generate("f"))
data.addSample(lib.generate("indumathi"),lib.generate("f"))
data.addSample(lib.generate("nivedha"),lib.generate("f"))
data.addSample(lib.generate("maheswari"),lib.generate("f"))
data.addSample(lib.generate("aishwarya"),lib.generate("f"))
data.addSample(lib.generate("arun"),lib.generate("m"))
data.addSample(lib.generate("bharadwaj"),lib.generate("m"))
data.addSample(lib.generate("kumar"),lib.generate("m"))
data.addSample(lib.generate("raja"),lib.generate("m"))
data.addSample(lib.generate("sundar"),lib.generate("m"))
data.addSample(lib.generate("giridhar"),lib.generate("m"))
data.addSample(lib.generate("subramani"),lib.generate("m"))
t = BackpropTrainer(n, data, learningrate = 0.1, momentum = 0, verbose = True)

for epoch in range(0,1000):
    t.train()
print "suresh",lib.reverse(n.activate(lib.generate("suresh")))

f = open('tmp_pickle.pic', 'wb')
pickle.dump(n, f)
f.close()
#
#f = open('tmp_pickle.pic', 'rb')
#i = pickle.load(f)
#f.close()