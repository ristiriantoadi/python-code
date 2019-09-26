import math


def init_ann():
    hidden_layer = [{'weight': [-0.5, 1, -0.5],
                     'output':[],
                     'tao':[],
                     'status':"2"},
                    {'weight': [-0.5, 1, -1],
                     'output':[],
                     'tao':[],
                     'status':"3"}]
    output_layer = [{'weight': [0.1, -0.5, 1],
                     'output':[],
                     'tao':[],
                     'status':"4"}]
    network = list()
    network.append(hidden_layer)
    network.append(output_layer)
    return network


def summation(weights, inputs):
    summation = weights[-1]  # bias
    # print("Bias: "+str(summation))
    for i in range(len(weights)-1):
        summation += weights[i]*inputs[i]
        # print(str(weights[i])+" x "+str(inputs[i]))
        # print(str(inputs[i])+" x "+str(inputs[i]))
    return summation


def activation(weights, inputs):
    sum = summation(weights, inputs)
    # print("Sum: "+str(sum))
    return 1/(1+math.exp(-sum))


def tao(y, t):
    # print("y: "+str(y))
    # print("t: "+str(t))
    return y*(1-y)*(t-y)


# def back_propagate(network, target, iteration):
#     for i in reversed(range(len(network))):
#         layer = network[i]
#         print("layer: "+str(i))
#         errors = list()
#         if i != len(network)-1:
#             for j in range(len(layer)):
#                 error = 0.0
#                 for neuron in network[i+1]:
#                     error += (neuron['weight'][j]*neuron['tao']
#                               [iteration])  # error in each neuron
#                     print("Neuron: "+str(j))
#                     print("Neuron+1 weight: "+str(neuron['weight'][j]))
#                     print("Neuron+1 tao: "+str(neuron['tao'][iteration]))
#                 errors.append(error)  # error of each neuron in a layer
#         else:  # yang ini udah bener
#             for j in range(len(layer)):
#                 neuron = layer[j]
#                 errors.append(target-neuron['output'][iteration])
#         for j in range(len(layer)):
#             neuron = layer[j]
#             # print("Neuron: "+str(j))
#             print("Output: "+str(neuron['output']
#                                  [iteration]))
#             print("Tao: "+str(errors[j]*neuron['output']
#                               [iteration]*(1.0-neuron['output'][iteration])))
#             neuron['tao'].append(errors[j]*neuron['output']
#                                  [iteration]*(1.0-neuron['output'][iteration]))
#     return network

def back_propagate(network, target, iteration):
    for i in reversed(range(len(network))):
        layer = network[i]
        for j in range(len(target)):
            if i != len(network)-1:
                for k in range(len(layer))


def forward_propagate(network, row_of_data):
    # start with input layer, which is just row_of data
    # print("Data masukan: ")
    inputs = list()
    for i in range(len(row_of_data)-1):
        inputs.append(row_of_data[i])
    # print(inputs)
    new_network = list()
    num_of_layer = 0
    for layer in network:
        new_input = list()
        new_layer = list()
        # print(num_of_layer)
        for neuron in layer:
            # print("Layer "+str(num_of_layer))
            output = activation(neuron['weight'], inputs)
            # print("Output "+str(output))
            neuron['output'].append(output)
            new_input.append(output)
            new_layer.append(neuron)
        inputs = new_input
        new_network.append(new_layer)
        num_of_layer += 1
    # new_network=list()
    # new_network.append(new_)
    return new_network


network = init_ann()

data = [[0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
        ]


def print_network(network):
    for layer in network:
        for neuron in layer:
            print(neuron)


# print_network(network)
network = forward_propagate(network, data[0])
network = back_propagate(network, data, 0)
print_network(network)
