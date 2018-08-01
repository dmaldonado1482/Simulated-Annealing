from random import shuffle, randint, random
from math import sqrt, exp


import sys
print(sys.argv[0])  # prints python script .py
print(sys.argv[1])  # prints var1   .tsp


def parse_tour(initial):
    # tour = []
    # with open(initial, 'r') as f:
    #     # for i in range(7):     For dj38.tsp     # for dj38.tsp
    #     for i in range(4):  # 7
    #         f.readline()
    #
    #     # dimensions, num_of_cities = f.readline().split('DIMENSION : ')    # for dj38.tsp
    #     dimensions, num_of_cities = f.readline().split('DIMENSION : ')
    #     cities = int(num_of_cities)  # how many cities in the TSP file

    tour = []
    dimension = 0
    with open(initial, 'r') as f:
        for line in f:
            if line.startswith('DIMENSION : '):
                x, dimensions = line.split('DIMENSION : ')
                dimension = int(dimensions)
                break

        f.readline()
        f.readline()

        for i in range(dimension):
            city_index, coord1, coord2 = f.readline().split(' ')
            index = int(city_index) - 1
            x1 = float(coord1)
            y1 = float(coord2)
            city = (index, x1, y1)
            tour.append(city)

    return tour


def distance(city1, city2):
    d = int(round(sqrt((city1[1] - city2[1]) * (city1[1] - city2[1]) + (city1[2] - city2[2]) * (city1[2] - city2[2]))))
    return d


def fitness(tour):
    e = 0
    for i in range(len(tour)):
        e += distance(tour[i], tour[i - 1])
    return e


def simulated_annealing(initial_tour):
    state = list(initial_tour)
    fit_state = fitness(state)

    temp_max = 25000
    temp_min = 2.5

    while temp_max > temp_min:
        a = randint(0, len(state) - 1)
        b = randint(0, len(state) - 1)
        neighbor = list(state)
        neighbor[a], neighbor[b] = neighbor[b], neighbor[a]  # randomly selected neighbor
        fit_neighbor = fitness(neighbor)  # fitness of neighbor

        if fit_neighbor < fit_state:
            fit_state = fit_neighbor
            state = list(neighbor)
        else:
            difference = fit_neighbor - fit_state

            if difference < 0 or exp(-difference / temp_max) > random():
                fit_state = fit_neighbor
                state = list(neighbor)
        temp_max = temp_max * .9999

        print(fit_state)

        shortest_tour = []
        for i in range(len(state)):
            shortest_tour.append(state[i][0])

    return shortest_tour


filename = sys.argv[1]
tour = parse_tour(filename)
# tour = parse_tour('uy734.tsp')
# tour = parse_tour('qa194.tsp')
shuffle(tour)
fitness(tour)

shortest = simulated_annealing(tour)
print('\n')
print(shortest)
