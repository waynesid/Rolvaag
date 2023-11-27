import torch.nn as nn
class NeuralNetworkClassificationModel(nn.Module):
    def __init__(self,input_dim,output_dim):
        super(NeuralNetworkClassificationModel,self).__init__()
        self.input_layer    = nn.Linear(input_dim,32)
        self.hidden_layer1  = nn.Linear(32,64)
        self.output_layer   = nn.Linear(64,output_dim)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)  # Add this line
    
    def forward(self,x):
        out =  self.relu(self.input_layer(x))
        out =  self.relu(self.hidden_layer1(out))
        out =  self.output_layer(out)
        out =  self.softmax(out)  # Add this line
        return out