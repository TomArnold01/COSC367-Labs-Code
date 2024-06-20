import random
def roulette_wheel_select(population, fitness, r):
    total_fitness = sum(fitness(i) for i in population)
    N = r * total_fitness
    total = 0
    for i in range(total_fitness):
        total += fitness(population[i])
        if N <= total:
            return population[i]
    return population[-1]




def main():

    population = ['a', 'b']

    def fitness(x):
        return 1 # everyone has the same fitness

    for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
        print(roulette_wheel_select(population, fitness, r))

    population = [0, 1, 2]

    def fitness(x):
        return x

    for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
        print(roulette_wheel_select(population, fitness, r))


if __name__ == "__main__":
    main()
