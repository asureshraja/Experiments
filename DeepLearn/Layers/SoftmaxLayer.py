import numpy as np
import LinearLayer
class SoftmaxLayer(LinearLayer.LinearLayer):
    def __init__(numUnits):
        super(numUnits)

    def getlayderiv(self,layerActivities):
        derivative=np.ones(self.numUnits)
        return derivative

    def getActivationProbabilities(sw_Sum):
        activation_probabilities=sw_Sum
        for i in range(0,len(activation_probabilities)):
            denominator=0
            numUnits=self.getNumUnits()
            for j in range(0,numUnits):
                activation_probabilities[i][j]=np.exp(activation_probabilities[i][j]+self.biases[j])
                denominator += activation_probabilities[i][j]

            for j in range(0,numUnits):
                activation_probabilities[i][j] /= denominator;

        return activation_probabilities
