def max_value(tree):
    if type(tree) is int:
        return tree
    
    k = max([min_value(tree[a]) for a in range(len(tree))])
    return k

def min_value(tree):

    if type(tree) is int:
        return tree
    k = min([max_value(tree[a]) for a in range(len(tree))])
    return k


def  max_action_value(game_tree):
    """
    given a tree return (best action, utility)
    """
    if type(game_tree) == int:
        return None, game_tree
    else:
        result = []
        for index, i in enumerate(game_tree):
            utility = min_value(i)
            result.append((index, utility))
        return max(result, key=lambda x: x[1])


def min_action_value(game_tree):
    """return a tuple where the first element is the best min action to consider,
    the second element ois the utility value"""
    if type(game_tree) == int:
        return None, game_tree
    else:
        result = []
        for index, tree in enumerate(game_tree):
            min_utility = max_value(tree)
            result.append((index, min_utility))
        return min(result, key=lambda x: x[1])
def main():
    

    game_tree = [2, [-3, 1], 4, 1]

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)


    game_tree = 3

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)

    game_tree = [1, 2, [3]]

    action, value = min_action_value(game_tree)
    print("Best action if playing min:", action)
    print("Best guaranteed utility:", value)
    print()
    action, value = max_action_value(game_tree)
    print("Best action if playing max:", action)
    print("Best guaranteed utility:", value)

if __name__ == "__main__":
    main()
