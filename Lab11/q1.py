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



def main():
    game_tree = 3

    print("Root utility for minimiser:", min_value(game_tree))
    print("Root utility for maximiser:", max_value(game_tree))

    game_tree = [1, 2, 3]

    print("Root utility for minimiser:", min_value(game_tree))
    print("Root utility for maximiser:", max_value(game_tree))

    game_tree = [1, 2, [3]]

    print(min_value(game_tree))
    print(max_value(game_tree))

    game_tree = [[1, 2], [3]]

    print(min_value(game_tree))
    print(max_value(game_tree))


if __name__ == "__main__":
    main()
