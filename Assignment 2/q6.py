import random
def evaluate(expression, bindings):
    if type(expression) == int:
        return expression
    elif type(expression) == str and expression in bindings:
        return bindings[expression]
    else:
        function = bindings[expression[0]]
        return function(evaluate(expression[1], bindings), evaluate(expression[2], bindings)) 

def random_expression(function_symbols, leaves, max_depth, depth=0):
    if depth==max_depth or random.random() < 0.5: 
        return random.choice(leaves)
    else:
        return [random.choice(function_symbols)] + [random_expression(function_symbols, leaves, max_depth, depth+1) for _ in range(2)]


def generate_rest(initial_sequence, expression, length):
    bindings = {'i' : len(initial_sequence), 
                'y' : initial_sequence[-1], 
                'x' : initial_sequence[-2],
                '*' : lambda x, y : x * y,
                '+' : lambda x, y : x + y,
                '-' : lambda x, y : x - y}
    result = []
    
    for item in range(length):
        expres = evaluate(expression, bindings)
        result.append(expres)        
        bindings['x'] = bindings['y']
        bindings['y'] = expres
        bindings['i'] = item + len(initial_sequence) + 1
    return result

def predict_rest(sequence):
    finsihed = False
    function_symbols = ['*', '+', '-']
    leaves = ['x', 'y', 'i'] + list(range(-2, 3))
    max_depth = 3
    
    while not finsihed:
        expression = random_expression(function_symbols, leaves, max_depth)
        create_test = generate_rest(sequence[:3], expression, len(sequence) - 3)
        if create_test == sequence[3:]:
            break
    return generate_rest(sequence, expression, 5)
        
def main():
    sequence = [0, 1, 2, 3, 4, 5, 6, 7]
    the_rest = predict_rest(sequence)
    print(sequence)
    print(the_rest)


    sequence = [0, 2, 4, 6, 8, 10, 12, 14]
    print(predict_rest(sequence))


    sequence = [31, 29, 27, 25, 23, 21]
    print(predict_rest(sequence))
   

    sequence = [0, 1, 4, 9, 16, 25, 36, 49]
    print(predict_rest(sequence))


    sequence = [3, 2, 3, 6, 11, 18, 27, 38]
    print(predict_rest(sequence))


    sequence =  [0, 1, 1, 2, 3, 5, 8, 13]
    print(predict_rest(sequence))


    sequence = [0, -1, 1, 0, 1, -1, 2, -1]
    print(predict_rest(sequence))


    sequence = [1, 3, -5, 13, -31, 75, -181, 437]
    print(predict_rest(sequence))

if __name__ == "__main__":
    main()