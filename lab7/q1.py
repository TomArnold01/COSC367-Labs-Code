


def n_queens_neighbours(state):
    states = []
    for i in range(len(state)+1):
        for j in range(i+1, len(state)):
            hold = list(state)
            hold[i], hold[j] = hold[j], hold[i]
            states.append(tuple(hold))
    return sorted(states)




def main():

    print(n_queens_neighbours((1, 2)))


    print(n_queens_neighbours((1, 3, 2)))

    print(n_queens_neighbours((1, 2, 3)))

    print(n_queens_neighbours((1,)))

    for neighbour in n_queens_neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
        print(neighbour)

    
if __name__ == "__main__":
    main()
