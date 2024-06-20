def evaluate(node, alpha, beta, is_max_node=True):
    if isinstance(node, int):  # Check if the node is a leaf node (an integer in this case).
        return node
    if is_max_node:
        for child in node:
            alpha = max(alpha, evaluate(child, alpha, beta, is_max_node=False))
            if beta <= alpha:
                print(f"Pruning at alpha = {alpha} and beta = {beta}")
                return alpha
        return alpha
    else:
        for child in node:
            beta = min(beta, evaluate(child, alpha, beta, is_max_node=True))
            if beta <= alpha:
                print(f"Pruning at alpha = {alpha} and beta = {beta}")
                return beta
        return beta

# You can call the evaluate function with your game tree represented as a nested list and specify is_max_node as True.
game_tree = [[0, [6 , 3], 11], [8, -8, -10]]
alpha = float('-inf')
beta = float('inf')
result = evaluate(game_tree, alpha, beta, is_max_node=True)
print(result)  # This will print the result of evaluating the game tree starting with a maximizing node.
