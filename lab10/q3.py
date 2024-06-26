def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        # Complete (a line or two)
        weighted_sum = sum(input[i] * weights[i] for i in range(len(input))) + bias
        if weighted_sum >= 0:
            return 1
        else:
            return 0
        # Note: we are masking the built-in input function but that is
        # fine since this only happens in the scope of this function and the
        # built-in input is not needed here.
        
        # what the perceptron should return
    
    return perceptron # this line is fine


def main():

    weights = [2, -4]
    bias = 0
    perceptron = construct_perceptron(weights, bias)

    print(perceptron([1, 1]))
    print(perceptron([2, 1]))
    print(perceptron([3, 1]))
    print(perceptron([-1, -1]))

if __name__ == "__main__":
    main()