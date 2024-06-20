



def greedy_descent(initial_state, neighbours, cost):
    result = [initial_state]
    current = (cost(initial_state), initial_state)
    previous = None
    while current != previous:      
        previous = current
        current_neighbours = [(cost(i), i) for i in neighbours(current[1])]
        if len(current_neighbours) == 0:
            break
        else:
            min_neighbour = min(current_neighbours, key=lambda x: x[0])
            if current[0] > min_neighbour[0]:
                result.append(min_neighbour[1])
                current = min_neighbour         
        
    return result

def main():

    def cost(x):
        return x**2

    def neighbours(x):
        return [x - 1, x + 1]

    for state in greedy_descent(4, neighbours, cost):
        print(state)


    def cost(x):
        return x**2

    def neighbours(x):
        return [x - 1, x + 1]

    for state in greedy_descent(-6.75, neighbours, cost):
        print(state)



if __name__ == "__main__":
    main()
