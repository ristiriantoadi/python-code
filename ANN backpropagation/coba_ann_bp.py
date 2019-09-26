import math


def initialize_ann():
    network = list()
    hidden_layer = [
        {'weights': [-0.5, 1, -0.5], 'output':[]},
        {'weights': [-0.5, 1, -1], 'output':[]},
    ]
    network.append(hidden_layer)
    output_layer = [
        {'weights': [0.1, -0.5, 1], 'output':[]}
    ]
    network.append(output_layer)
    return network


# network = initialize_ann()
# print(network)


def activation(summation):
    return 1/(1+math.exp(-summation))


# print(activation(-0.5))


def tao(y, t):  # transfer derivative plus error backpropagation
    return y*(1-y)*(t-y)

    # transfer derivative is y*(1-y)
    # error backpropagation is (t-y)*transfer derivative


def hidden_layer_tao(y, tao, w):
    return y*(1-y)*(tao*w)


def updateStep(l_rate, output_prev_layer, tao):
    return l_rate*output_prev_layer*tao


# def training(network, dataset):

# def backward_propagation(network, target):

#     for i in reversed(range(len(network))):
#         layer = network[i]
#         errors = list()
#         # if i != len(network)-1:#meaning this is in the hidden layer
#         #     for j in range(len(layer)):
#         #         error = 0.0
#         #         for neuron in network[i+1]:

#         # for j in range(length(layer)):
#         #     neuron = layer[j]
#         if i == len(network)-1:  # meaning this is the outermost layer
#             for neuron in layer:
#                 neuron.tao = tao(neuron.output, target[i])
#         else:
#             for neuron in layer:
#                 hidden_layer_tao(neuron.output,)


# def training(dataset, network, l_rate, n_epoch):
#     for epoch in range(n_epoch):
#         for row in dataset:
#             forward_propagation(network, row, row_number)


# def forward_propagation(network, row,row_number):
#     inputs = list()
#     for i in range(len(row)-1):
#         inputs.append(row[i])
#     # print(inputs)
#     for layer in network:
#         new_inputs = []
#         for neuron in layer:
#             summation = activate(neuron['weights'], inputs)
#             neuron['output'][row_number] = activation(summation)
#             new_inputs.append(neuron)
#         inputs = new_inputs
#     return inputs

# def forward_propagation(network, row, row_number):
#     new_network = list()  # this represent a single network
#     inputs = list()  # this is for each row of input
#     for i in range(len(row)-1):
#         inputs.append(row[i])
#     for layer in network:
#         new_inputs = []  # this represent a single layer
#         for neuron in layer:
#             summation = activate(neuron['weights'], inputs)
#             neuron['output'][row_number] = activation(summation)
#             new_inputs.append(neuron)
#         new_network.append(new_inputs)  # this add the layer as it is
#         # this simply use the layer as the next input
#         inputs = new_inputs['output']

def forward_propagation(network, row, row_number):
    new_network = list()
    inputs = list()
    for i in range(len(row)-1):
        inputs.append(row[i])
    for layer in network:
        new_inputs = list()
        new_layer = list()
        for neuron in layer:
            summation = activate(neuron['weights'], inputs)
            neuron['output'].append(activation(summation))
            new_inputs.append(neuron['output'][row_number])
            new_layer.append(neuron)
        inputs = new_inputs
        new_network.append(new_layer)
    return new_network


def activate(weights, inputs):
    summation = weights[-1]
    for i in range(len(weights)-1):
        summation += weights[i]*inputs[i]
    return summation


network = initialize_ann()
# print(network)
data = [[0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
        ]
out = forward_propagation(network, data[0], 0)
print(out[0])
