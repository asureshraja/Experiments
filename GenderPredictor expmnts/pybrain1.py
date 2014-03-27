###
# xor.py
#
# author: Kristina Striegnitz
#
# version: 3/3/2010
#
# Simple example of training a neural network calculating XOR using
# the pybrain package.
###
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer


def make_dataset():
    """
    Creates a set of training data.
    """
    data = SupervisedDataSet(2,1)

    data.addSample([1,1],[0])
    data.addSample([1,0],[1])
    data.addSample([0,1],[1])
    data.addSample([0,0],[0])

    return data


def training(d):
    """
    Builds a network and trains it.
    """
    n = buildNetwork(d.indim, 4, d.outdim)
    t = BackpropTrainer(n, d, learningrate = 0.01, momentum = 0.99, verbose = True)
    for epoch in range(0,1000):
        t.train()
    return t


def test(trained):
    """
    Builds a new test dataset and tests the trained network on it.
    """
    testdata = SupervisedDataSet(2,1)
    testdata.addSample([1,1],[0])
    testdata.addSample([1,0],[1])
    testdata.addSample([0,1],[1])
    testdata.addSample([0,0],[0])
    print(testdata)
    print(trained.testOnClassData())


def run():
    """
    Use this function to run build, train, and test your neural network.
    """
    trainingdata = make_dataset()
    trained = training(trainingdata)
    test(trained)
run()