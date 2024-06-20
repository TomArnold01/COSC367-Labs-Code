def depth(expression):
    result = 0
    if type(expression) != list:
        return 0
    else:
        second_ele = depth(expression[1])
        thrid_ele = depth(expression[2])
        if second_ele > thrid_ele:
            return depth(expression[1]) + 1
        else:
            return depth(expression[2]) + 1


def main():
    expression = 12
    print(depth(expression))
    
    expression = 'weight'
    print(depth(expression))

    expression = ['add', 12, 'x']
    print(depth(expression))

    expression = ['add', ['add', 22, 'y'], 'x']
    print(depth(expression))
    
    expression = ['+', ['*', 2, 'i'], ['*', ['*', -3, ['*', -3, 'x']],'x']]
    print(depth(expression))
if __name__ == "__main__":
    main()



