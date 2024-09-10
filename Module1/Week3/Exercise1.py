import torch
import torch.nn as nn

data = torch.Tensor([1,2,3])

# softmax_function = nn.Softmax(dim = 0)
# output = softmax_function(data)
# output

class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        total = x_exp.sum(0, keepdims = True)
        return x_exp/total

class StableSoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x, dim = 0)
        x_exp = torch.exp(x-c.values)
        total = x_exp.sum(0, keepdims = True)
        return x_exp/total

my_softmax = StableSoftmax()
output = my_softmax.forward(data)
output