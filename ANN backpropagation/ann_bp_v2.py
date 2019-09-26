import math


def init_ann():
    hidden_layer = [{'weights': [-0.5, 1, -0.5], 'output':[], 'delta':[], 'delta_avg':[], 'delta_bias':0},
                    {'weights': [-0.5, 1, -1], 'output':[], 'delta':[], 'delta_avg':[], 'delta_bias':0}]
    output_layer = [{'weights': [0.1, -0.5, 1],
                     'output':[], 'delta':[], 'delta_avg':[], 'delta_bias':0}]
    network = list()
    network.append(hidden_layer)
    network.append(output_layer)
    return network


def calculate_delta_hidden_layer_per_row(row, network, iteration):
    layer = network[0]
    # errors = list()
    j = 0
    for neuron in layer:
        error = 0
        for neuron_next_layer in network[0+1]:
            error += neuron_next_layer['delta_avg'] * \
                neuron_next_layer['weights'][j]
        # errors.append(error)
        neuron['delta'].append(error*neuron['output']
                               [iteration]*(1.0-neuron['output'][iteration]))
        j = j+1
    return network


def calculate_delta_outer_layer_per_row(row, network, iteration):
    i = len(network)-1
    new_network = network
    layer = new_network[i]
    # errors = list()
    for neuron in layer:
        errors = row[-1]-neuron['output'][iteration]
        neuron['delta'].append(errors*neuron['output']
                               [iteration]*(1.0-neuron['output'][iteration]))
    return new_network
    # return 5+10


def summing_function(weights, data):
    summation = weights[-1]
    for i in range(len(weights)-1):
        summation += weights[i]*data[i]
    return summation


def activation_function(summation):
    return 1/(1+math.exp(-summation))


def forward_propagate_per_row(data, network):
    # do it per layer
    inputs = data
    new_network = list()
    for layer in network:
        new_input = list()
        new_layer = list()
        for neuron in layer:
            summation = summing_function(neuron['weights'], inputs)
            output = activation_function(summation)
            neuron['output'].append(output)
            new_input.append(output)
            new_layer.append(neuron)
        inputs = new_input
        new_network.append(new_layer)
    return new_network


# def calculate_d(row, network, iteration):
#     i = len(network)-1
#     # layer = network[i]
#     another_network = network
#     layer = another_network[i]
#     # errors = list()
#     for neuron in layer:
#         errors = row[-1]-neuron['output'][iteration]
#         neuron['delta'].append(errors*neuron['output'][iteration]*(1.0-neuron['output'][iteration])
#     return network

def calculate_avg(deltas):
    sum = 0
    for i in deltas:
        sum += i
    avg = sum/len(deltas)
    return avg


def calculate_delta_outer_layer(dataset, network):
    i = len(network)-1
    iteration = 0
    for row in dataset:
        network = calculate_delta_outer_layer_per_row(row, network, iteration)
        iteration += 1
    for neuron in network[i]:
        neuron['delta_avg'] = calculate_avg(neuron['delta'])
    return network


def calculate_delta_hidden_layer(dataset, network):
    iteration = 0
    for row in dataset:
        network = calculate_delta_hidden_layer_per_row(row, network, iteration)
        iteration += 1
    for neuron in network[0]:
        neuron['delta_avg'] = calculate_avg(neuron['delta'])
    return network


def calculate_bias_outer_layer(network):
    for neuron in network[len(network)-1]:
        delta_bias_sum = 0
        for delta in neuron['delta']:
            delta_bias_sum += -1*delta*neuron['weights'][-1]
        delta_bias_average = delta_bias_sum/len(neuron['delta'])
        neuron['delta_bias'] = delta_bias_average
    return network


def calculate_bias_hidden_layer(network):
    for neuron in network[0]:
        delta_bias_sum = 0
        for delta in neuron['delta']:
            delta_bias_sum += -1*delta*neuron['weights'][-1]
        delta_bias_average = delta_bias_sum/len(neuron['delta'])
        neuron['delta_bias'] = delta_bias_average
    return network


def update_neuron_weight(neuron, inputs):
    delta = 0.0
    for i in range(len(inputs)):
        delta += -1*inputs[i]*neuron['delta_avg']
    delta_weight_avg = delta/len(inputs)
    neuron


def update(dataset, network):
    new_network = list()
    for l in range(len(network)):
        layer = network[l]
        new_layer = list()
        for n in range(len(layer)):
            inputs = list()
            neuron = layer[n]
            if l == 0:
                for row in dataset:
                    inputs.append(row[n])
                    # inputs.append(dataset)
            neuron = update_neuron_weight(neuron, inputs)
            new_layer.append(neuron)
        new_network.append(new_layer)
    return new_network

# def update(dataset, network):
#     for l in range(len(network)):
#         layer = network[l]
#         inputs = list()
#         if l == 0:
#             for n in range(len(layer)):
#                 for i in range(len(dataset)):
#                     inputs.append(dataset[i][n])
#             # something happen hidden_layer
#                 print(inputs)
#         # else:

#             # def update(network, dataset):
#             #     for i in range(len(network)):
#             #         inputs =
#             #         if i != 0:
#             #             inputs = [neuron['output'][0] for neuron in network[i-1]]
#             #         for neuron in network[i]:
#             #             for j in range(len(inputs)):
#             #                 neuron['weights'][j] += -1*neuron['delta_avg']*inputs[j]
#             #             neuron['weights'][-1] += -1*neuron[delta_bias]


def back_propagate(dataset, network):
    # calculate per layer
    for i in reversed(range(len(network))):
        layer = network[i]
        if i != len(network)-1:
            # print("under contruction")
            network = calculate_delta_hidden_layer(dataset, network)
            calculate_bias_hidden_layer(network)
        else:
            network = calculate_delta_outer_layer(dataset, network)
            # print("Delta outer layer: ")
            # print(network)
            calculate_bias_outer_layer(network)
    # update(network)
    return network


def training(dataset, network, n_epoch):
    for epoch in range(n_epoch):
        network = forward_propagate(dataset, network)
        network = back_propagate(dataset, network)
        network = update(network, dataset)
    return network


def forward_propagate(dataset, network):

    for row in dataset:
        inputs = list()
        for i in range(len(row)-1):
            inputs.append(row[i])
        network = forward_propagate_per_row(inputs, network)
    return network


data = [[0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
        ]
network = init_ann()
# network = forward_propagate(data, network)
# network = back_propagate(data, network)
# print(network)
update(data, network)
