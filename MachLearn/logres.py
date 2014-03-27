import numpy as np

def sigmoid(x):
    return 1. / (1 + np.exp(-x))


def softmax(x):
    e = np.exp(x - np.max(x))  # prevent overflow
    if e.ndim == 1:
        return e / np.sum(e, axis=0)
    else:
        return e / np.array([np.sum(e, axis=1)]).T  # ndim = 2


class logreg:
    def __init__(self,input,output):
        self.input=np.array(input)
        self.output=np.array(output)
        self.noofinput=self.input.shape[1]
        self.noofoutput=self.output.shape[1]
        self.weights=np.zeros((self.noofinput,self.noofoutput))
        self.bias=np.zeros(self.noofoutput)

    def fit(self,epoch=100,lr=0.1,L2_reg=0.00):
        for epoch in xrange(epoch):
            prob = softmax(np.dot(self.input, self.weights) + self.bias)
            error = self.output - prob
            self.weights += lr * np.dot(self.input.T, error) - lr * L2_reg * self.weights
            self.bias += lr * np.mean(error, axis=0)
            lr=lr*0.98

    def predict(self, x):
        return softmax(np.dot(self.input, self.weights) + self.bias)

x = numpy.array([[1,1,1,0,0,0],
                 [1,0,1,0,0,0],
                 [1,1,1,0,0,0],
                 [0,0,1,1,1,0],
                 [0,0,1,1,0,0],
                 [0,0,1,1,1,0]])
y = numpy.array([[1, 0],
                 [1, 0],
                 [1, 0],
                 [0, 1],
                 [0, 1],
                 [0, 1]])

lr=logreg(x,y)
lr.fit()
print lr.predict(x)
