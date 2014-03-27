from abc import ABCMeta, abstractmethod
import numpy as np
class LayerStochastic:

    @abstractmethod
    def generateData(self,activation_probabilities):
        pass
