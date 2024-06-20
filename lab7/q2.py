
def n_queens_cost(state):
    count = 0
    for i in range(len(state) + 1):

        for j in range(i + 1, len(state)):

            if abs(state[i] - state[j]) == abs(i - j): 
                count += 1

    return count    



def main():

    print(n_queens_cost((1, 2)))

    print(n_queens_cost((1, 3, 2)))

    print(n_queens_cost((1, 2, 3)))

    print(n_queens_cost((1,)))

    print(n_queens_cost((1, 2, 3, 4, 5, 6, 7, 8)))

    print(n_queens_cost((2, 3, 1, 4)))
    
if __name__ == "__main__":
    main()
