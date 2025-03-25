from itertools import pairwise

def total_distance(path, distance):
    total_distance = 0
    for i in pairwise(path):
        total_distance += distance(i[0], i[1])
    return total_distance