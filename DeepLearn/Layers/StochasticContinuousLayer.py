import numpy as np
import Layer
class StochasticContinuousLayer(Layer.Layer):
    DEFAULT_UPPERBOUND = 1.0
    DEFAULT_LOWERBOUND = 0.0
    DEFAULT_NOISEVOLUME=0.1
    def __init__(numUnits,upper_bound=DEFAULT_UPPERBOUND,lower_bound=DEFAULT_LOWERBOUND):
        self.noiseVolume=DEFAULT_NOISEVOLUME
        self.upper_bound=upper_bound
        self.lower_bound=lower_bound

    def getActivationProbabilities(self,sw_Sum):
        activation_probabilities = sw_sum
        for i in range(0,len(sw_Sum)):
            for j in range(0,len(sw_Sum[i])):
                activation_probabilities[i][j] = 1.0 / (1 + np.exp(-1 * self.biases[i] * (sw_Sum[i][j] + self.noiseVolume * np.random.normal(0, 0.1, 1)[0])))
                activation_probabilities[i][j] = lower_bound + (upper_bound - lower_bound) * activation_probabilities[i][j]
        return activation_probabilities

