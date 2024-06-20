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


def main():
    perceptron = construct_perceptron([-1, 3], 2)
    inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
    targets = [0, 1, 1, 0]

    print(accuracy(perceptron, inputs, targets))

if __name__ == "__main__":
    main()