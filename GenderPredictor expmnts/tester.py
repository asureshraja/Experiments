import pickle
import sahelper as lib
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer,TanhLayer,SoftmaxLayer,GaussianLayer
from pybrain.structure import FullConnection
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
f = open('tmp_pickle.pic', 'rb')
i = pickle.load(f)
print "giri",i.activate(lib.generate("giri"))
f.close()