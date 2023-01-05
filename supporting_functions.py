import random

import numpy as np
from numpy import log

from variables import cities, route, distances


def discrete_distribution(elements, probabilities):
    return int(np.random.choice(elements, 1, p=list(probabilities)))


def normal_distribution(deviation):
    normal_var = abs(int(np.random.normal(0, deviation, 1)))
    return normal_var


def exponential_distribution():
    c = 0
    b = 0.05
    distribution_function = random.uniform(0, 1)
    number = c - (1 / b) * log(1 - distribution_function)
    return number


def generate_delay():
    delay_probability = 0.3
    random_number = np.random.random()
    if random_number < delay_probability:
        delay = normal_distribution(30)
    else:
        delay = normal_distribution(10) * (-1)
    return delay


def random_route(transfers, elements, probabilities):
    probability = (column(probabilities, 0))
    for x in range(transfers):
        cities.append(discrete_distribution(elements, probability))
        index = cities[x]
        probability = (column(probabilities, index))
        route.append(cities[x])
    cities.clear()


def route_length():
    distance = 0
    length = len(route) - 1
    for x in range(length):
        index_start = route[x]
        index_end = route[x + 1]
        distance = distances[index_start][index_end] + distance
    route.clear()
    route.append(0)
    return distance


def calculate_delay_sum(transfers):
    delay_sum = 0
    for x in range(transfers):
        delay_sum += generate_delay()
    return delay_sum


def column(matrix, i):
    return [row[i] for row in matrix]


def print_list(list_name):
    print()
    for x in range(len(list_name)):
        print(list_name[x])
    print()


def write_to_file(list_name):
    with open('project_data.txt', 'w') as f:
        for line in list_name:
            f.write("%s\n" % line)


def generate_numbers():
    twod_list = []
    for i in range(0, 10):
        new = []
        max_p = 1
        for j in range(0, 10):
            random_number = random.uniform(0, max_p)
            max_p = max_p - random_number
            new.append(random_number)
        twod_list.append(new)

    print(np.matrix(twod_list))
