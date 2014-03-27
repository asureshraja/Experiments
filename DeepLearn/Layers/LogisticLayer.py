import numpy as np
import Layer
class LogisticLayer(Layer.Layer):
    def __init__(numUnits):
        super(numUnits)

    def getlayderiv(self,layerActivities):
        derivative=np.ones(self.numUnits)
        for i in range(0,self.numUnits):
            derivative[i]=layerActivities[i]*(1 - layerActivities[i])
        return derivative

    def getActivationProbabilities(self,sw_Sum):
        activation_probabilities=sw_Sum
        for i in range(0,len(activation_probabilities)):
            for j in range(0,self.getNumOfUnits):
                activation_probabilities[i][j]=1.0 / (1 + np.exp(-sw_Sum[i][j] - self.biases[j]))
        return activation_probabilities

