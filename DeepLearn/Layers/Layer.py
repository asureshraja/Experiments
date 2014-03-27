from abc import ABCMeta, abstractmethod
import numpy as np
class Layer:
    __metaclass__ = ABCMeta
    DEFAULT_BIAS_LEARNING_RATE = 0.05
    DEFAULT_BIAS_MOMENTUM = 0.5
    DEFAULT_BIAS_WEIGHTCOST = 0.00002 * DEFAULT_BIAS_LEARNING_RATE

    def __init__(self,numUnits):
        self.biases=np.zeros(numUnits)
        self.biasIncrement=np.zeros(numUnits)
        self.learningRate=DEFAULT_BIAS_LEARNING_RATE
        self.weightCost=DEFAULT_BIAS_WEIGHTCOST
        self.momentum=DEFAULT_BIAS_MOMENTUM

    def changeNumUnits(self,newNumOfUnits):
        newBiases=np.zeros(newNumOfUnits)
        newBiasIncrements=np.zeros(newNumOfUnits)
        maxLength=min(len(newBiases),len(self.biases))
        for i in range(0,maxLength-1):
            newBiases[i]=self.biases[i]
            newBiasIncrements[i]=self.biasIncrement[i]
        self.biases=newBiases
        self.biasIncrement=newBiasIncrements

    def getLearningRate(self):
        return self.learningRate
    def setLearningRate(self,newLearningRate):
        self.learningRate=newLearningRate
    def getWeightCost(self):
        return self.weightCost
    def setWeightCost(self,newWeightCost):
        self.weightCost=newWeightCost
    def getMomentum(self):
        return self.momentum
    def setMomentum(self,newMomentum):
        self.momentum=newMomentum
    def getBiases(self):
        return self.biases
    def setBiases(self,newBiases):
        self.biases=newBiases
    def getBiasIncrement(self):
        return self.biasIncrement
    def setBiasIncrement(self,newBiasIncrement):
        self.biasIncrement=newBiasIncrement
    def getNumOfUnits(self):
        return len(biases)


    @abstractmethod
    def getLayDeri_layactiv(self,productSum):
        pass

    @abstractmethod
    def getLayDeri_batlayactiv(self,batchLayerActivities):
        #batchLayerActivities must be  two dimensional
        layerderivatives=[]
        for bla in batchLayerActivities:
            layerderivatives.append(getLayDeri_layactiv(bla))
        return layerderivatives

    @abstractmethod
    def getActivProb_actprob(self,activation_probabilities):
        batactiv=activation_probabilities
        return generateData(batactiv)[0]

    @abstractmethod
    def getActivProb_batactprob(self,activation_probabilities):
        pass

    @abstractmethod
    def generateData(self,activation_probabilities):
        pass

