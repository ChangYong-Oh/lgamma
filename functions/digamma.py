from torch import autograd
from .internals import polygamma

class Digamma(autograd.Function):
    def forward(self, input):
        self.save_for_backward(input)
        return polygamma(0, input)

    def backward(self, grad_output):
        input, = self.saved_tensors
        return grad_output * polygamma(1, input)
