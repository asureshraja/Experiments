import numpy as np
import Layer
class LinearLayer(Layer.Layer):
    def __init__(self,numUnits):
        super(numUnits)
    def getlayderiv(self,layerActivities):
        derivative=np.ones(self.numUnits)
        return derivative
    def getActivationProbabilities(self,productSum):
        activation_probabilities=productSum
        for i in range(0,len(activation_probabilities)):
            for j in range(0,self.getNumOfUnits):
                activation_probabilities[i][j]=self.biases[j]
        return activation_probabilities

