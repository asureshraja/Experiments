import numpy as np
import LinearLayer
class StochasticLinearLayer(LinearLayer.LinearLayer):
    def __init__(self,numUnits):
        super(numUnits)

    def generateData(self,activation_probabilities):
        generatedData=np.zeros((len(activation_probabilities),self.getNumUnits()))
        for i in range(0,len(generatedData)):
            for j in range(0,self.getNumUnits()):
                generatedData[i][j]=activation_probabilities[i][j]+np.random.normal(0, 0.1, 1)[0]
        return generatedData
