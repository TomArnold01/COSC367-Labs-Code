import random

def random_expression(function_symbols, leaves, max_depth, depth=0):
    if depth==max_depth or random.random() < 0.5: 
        return random.choice(leaves)
    else:
        return [random.choice(function_symbols)] + [random_expression(function_symbols, leaves, max_depth, depth+1) for _ in range(2)]

def main():
    # All the generated expressions must be valid

    function_symbols = ['f', 'g', 'h']
    constant_leaves =  list(range(-2, 3))
    variable_leaves = ['x', 'y', 'i']
    leaves = constant_leaves + variable_leaves
    max_depth = 4

    for _ in range(10000):
        expression = random_expression(function_symbols, leaves, max_depth)
        if not is_valid_expression(expression, function_symbols, leaves):
            print("The following expression is not valid:\n", expression)
            break
    else:
        print("OK")

    function_symbols = ['f', 'g', 'h']
    leaves = ['x', 'y', 'i'] + list(range(-2, 3))
    max_depth = 4

    expressions = [random_expression(function_symbols, leaves, max_depth)
                for _ in range(10000)]

    # Out of 10000 expressions, at least 1000 must be distinct
    _check_distinctness(expressions)

    function_symbols = ['f', 'g', 'h']
    leaves = ['x', 'y', 'i'] + list(range(-2, 3))
    max_depth = 4

    expressions = [random_expression(function_symbols, leaves, max_depth)
                for _ in range(10000)]

    # Out of 10000 expressions, there must be at least 100 expressions
    # of depth 0, 100 of depth 1, ..., and 100 of depth 4.

    _check_diversity(expressions, max_depth)

if __name__ == "__main__":
    main()