def evaluate(expression, bindings):
    if type(expression) == int:
        return expression
    elif type(expression) == str and expression in bindings:
        return bindings[expression]
    else:
        function = bindings[expression[0]]
        return function(evaluate(expression[1], bindings), evaluate(expression[2], bindings)) 



def main():
    bindings = {}
    expression = 12
    print(evaluate(expression, bindings))

    bindings = {'x':5, 'y':10, 'time':15}
    expression = 'y'
    print(evaluate(expression, bindings))

    bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
    expression = ['add', 12, 'x']
    print(evaluate(expression, bindings))

    import operator
    bindings = dict(x = 5, y = 10, blah = 15, add = operator.add)
    expression = ['add', ['add', 22, 'y'], 'x']
    print(evaluate(expression, bindings))

if __name__ == "__main__":
    main()