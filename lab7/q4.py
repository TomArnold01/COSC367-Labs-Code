import random

def n_queens_neighbours(state):
    states = []
    for i in range(len(state)+1):
        for j in range(i+1, len(state)):
            hold = list(state)
            hold[i], hold[j] = hold[j], hold[i]
            states.append(tuple(hold))
    return sorted(states)


def n_queens_cost(state):
    count = 0
    for i in range(len(state) + 1):

        for j in range(i + 1, len(state)):

            if abs(state[i] - state[j]) == abs(i - j): 
                count += 1

    return count    


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


def greedy_descent_with_random_restart(random_state, neighbours, cost):
    done = False
    while not done:
        initial_state = random_state()
        states = greedy_descent(initial_state, neighbours, cost)
        for state in states:
            print(state)
            if cost(state) == 0:
                done = True
        if not done:
            print('RESTART')

def main():

    N = 6
    random.seed(0)

    def random_state():
        return tuple(random.sample(range(1,N+1), N))   

greedy_descent_with_random_restart(random_state, n_queens_neighbours, n_queens_cost)
if __name__ == "__main__":
    main()
