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

print("data: \n"+str(dataset))
print("weights: \n"+str(weights))
print("\n")


def act_function(dt):
    return 1.0 if dt >= 0.0 else 0.0


def testing(data, weights):
    for row in data:
        predicted = predict(row, weights)
        print("Excpected: "+str(row[-1])+", Predicted "+str(predicted))


def predict(row, weights):
    activation = weights[0]  # bias
    for i in range(len(row)-1):
        activation += weights[i+1]*row[i]
    y = act_function(activation)
    # print("Prediction: "+str(y))
    return y


out_act = act_function(-1)
# print(out_act)

# t = dataset[7]
# print(t)
# # print("\n")
# print(weights)
# prediction = predict(t, weights)
# print("Excpected "+str(t[-1])+", Predicted "+str(prediction))


def train_weights(train, l_rate, n_epoch):
    weights = [0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        print("Epoch: "+str(epoch))
        sum_error = 0.0
        row_num = 0
        for row in train:
            print("Row no: "+str(row_num))
            prediction = predict(row, weights)
            error = (row[-1]-prediction)
            sum_error += error**2
            weights[0] = weights[0]+l_rate*error
            # print(weights[0])
            for i in range(len(row)-1):
                weights[i+1] = weights[i+1]+l_rate*error*row[i]
                # print(weights[i+1])
            print(weights)
            row_num += 1
        print("lrate " +
              str(l_rate)+", error "+str(sum_error))
        print(weights)
    return weights


weights = train_weights(dataset, 0.1, 6)
testing(dataset, weights)
