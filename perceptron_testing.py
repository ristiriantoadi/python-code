dataset = [[2.7810836, 2.550537003, 0],
           [1.465489372, 2.362125076, 0],
           [3.396561688, 4.400293529, 0],
           [1.38807019, 1.850220317, 0],
           [3.06407232, 3.005305973, 0],
           [7.627531214, 2.759262235, 1],
           [5.332441248, 2.088626775, 1],
           [6.922596716, 1.77106367, 1],
           [8.675418651, -0.242068655, 1],
           [7.673756466, 3.508563011, 1]]

weights = [0.0, -1.0, 0.0]


def predict(data, weight):  # predict per row of data
    activation = weight[0]
    for i in range(len(data)-1):
        activation += weight[i+1]*data[i]
    y = activation_function(activation)
    return y


def activation_function(activation):
    return 1.0 if activation >= 0 else 0.0


# y = predict(dataset[3], weights)
# print("Prediction: "+str(y))
# print("Expected: "+str(dataset[2][-1]))
# print(activation_function(-2))

def train(training, l_rate, n_epoch):
    weights = [0.0 for i in range(len(training[0]))]
    for epoch in range(n_epoch):
        summing_error = 0.0
        for row in training:
            predicted = predict(row, weights)
            error = row[-1]-predicted
            summing_error += error**2
            weights[0] = weights[0]+l_rate*error
            for i in range(len(row)-1):
                weights[i+1] = weights[i+1]+l_rate*error*row[i]
        print("Epoch: "+str(epoch)+", l_rate: " +
              str(l_rate)+", error: "+str(summing_error))

    return weights


weights = train(dataset, 0.1, 6)
