import numpy as np
import LogisticLayer
class StochasticBinaryLayer(LogisticLayer.LogisticLayer):
    def __init__(self,numUnits):
        super(numUnits)

    def generateData(self,activation_probabilities):
        generatedData=np.zeros((len(activation_probabilities),self.getNumUnits()))
        for i in range(0,len(generatedData)):
            for j in range(0,self.getNumUnits):
                if(activation_probabilities[i][j]>0.50):
                    generatedData[i][j]=1
                else:
                    generatedData[i][j]=0
        return generatedData
