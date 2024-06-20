
def evaluate(expression, bindings):
    if type(expression) == int:
        return expression
    elif type(expression) == str and expression in bindings:
        return bindings[expression]
    else:
        function = bindings[expression[0]]
        return function(evaluate(expression[1], bindings), evaluate(expression[2], bindings)) 


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

def main():
    initial_sequence = [0, 1, 2]
    expression = 'i' 
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression,
                        length_to_generate))
   

    # no particular pattern, just an example expression
    initial_sequence = [-1, 1, 367]
    expression = 'i' 
    length_to_generate = 4
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))

    initial_sequence = [4, 6, 8, 10]
    expression = ['*', ['+', 'i', 2], 2]
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))

    initial_sequence = [4, 6, 8, 10]
    expression = ['+', 2, 'y']
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))


    initial_sequence = [0, 1]
    expression = 'x'
    length_to_generate = 6
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))


    # Fibonacci sequence
    initial_sequence = [0, 1]
    expression = ['+', 'x', 'y']
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))


    initial_sequence = [367, 367, 367]
    expression = 'y'
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
  

    # no pattern, just a demo
    initial_sequence = [0, 1, 2]
    expression = -1 
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
   

    initial_sequence = [0, 1, 2]
    expression = 'i'
    length_to_generate = 0
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    
if __name__ == "__main__":
    main()