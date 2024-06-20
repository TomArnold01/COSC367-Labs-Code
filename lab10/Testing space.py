def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        weighted_sum = sum(input[i] * weights[i] for i in range(len(input))) + bias
        if weighted_sum >= 0:
            return 1
        else:
            return 0
    return perceptron


def accuracy(classifier, inputs, expected_outputs):
    current = []

    for items in inputs:
        current.append(classifier(items))
    result = 1
    count = len(current)
    score_one = 1 / count
    for i in range(count):
        if current[i] != expected_outputs[i]:
            result -= score_one
    return result


def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    cur_weights = weights[:]
    for i in range(max_epochs):
        for example in training_examples:
            perceptron = construct_perceptron(cur_weights, bias)
            t = example[1]
            y = perceptron(example[0])
            w1 = cur_weights[0] + learning_rate * example[0][0] * (t - y)
            w2 = cur_weights[1] + learning_rate * example[0][1] * (t - y)
            cur_weights[0] = w1
            cur_weights[1] = w2
            bias = bias + learning_rate * (example[1] - y)
    return cur_weights, bias



def main():
    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
    ((0, 0), 0),
    ((0, 1), 0),
    ((1, 0), 0),
    ((1, 1), 1),
    ]
    max_epochs = 50

    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")

    perceptron = construct_perceptron(weights, bias)

    print(perceptron((0,0)))
    print(perceptron((0,1)))
    print(perceptron((1,0)))
    print(perceptron((1,1)))
    print(perceptron((2,2)))
    print(perceptron((-3,-3)))
    print(perceptron((3,-1)))

    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
    ((0, 0), 0),
    ((0, 1), 1),
    ((1, 0), 1),
    ((1, 1), 0),
    ]
    max_epochs = 50

    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")
if __name__ == "__main__":
    main()