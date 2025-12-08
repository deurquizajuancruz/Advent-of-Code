from sys import stdin
import math


def read_input() -> list:
    all_coordinates: list = []
    all_coordinates.append(list(map(int, stdin.readline().strip().split(","))))
    line: str = stdin.readline().strip()
    while line:
        all_coordinates.append(list(map(int, line.split(","))))
        line = stdin.readline().strip()
    return all_coordinates


def calculate_distance(box1: list, box2: list) -> float:
    return math.sqrt(
        pow(box1[0] - box2[0], 2)
        + pow(box1[1] - box2[1], 2)
        + pow(box1[2] - box2[2], 2)
    )


all_coordinates: list = read_input()
min: float = float("inf")
index: int = 1
all_distances: list = []

for coordinate in all_coordinates:
    second_index: int = index
    second_min: int = 0
    min: float = float("inf")
    for compare_coordinates in all_coordinates[index:]:
        distance: float = calculate_distance(coordinate, compare_coordinates)
        second_index += 1
        all_distances.append((distance, index - 1, second_index - 1))
    index += 1

all_distances = sorted(all_distances, key=lambda x: x[0])

list_sets: list = []


def what_circuit(index: int) -> set | None:
    for set in list_sets:
        if index in set:
            return set
    return None


for i in range(1000):
    circuit1: set | None = what_circuit(all_distances[i][1])
    circuit2: set | None = what_circuit(all_distances[i][2])
    if not circuit1 and not circuit2:
        list_sets.append(set((all_distances[i][1], all_distances[i][2])))
    elif circuit1 and not circuit2:
        circuit1.add(all_distances[i][2])
    elif circuit2 and not circuit1:
        circuit2.add(all_distances[i][1])
    elif circuit1 != circuit2:
        circuit1.update(circuit2)  # type: ignore
        list_sets.remove(circuit2)


for i in range(1000):
    if not what_circuit(i):
        list_sets.append({i})


list_sets = sorted(list_sets, key=lambda circuito: len(circuito), reverse=True)
print(len(list_sets[0]) * len(list_sets[1]) * len(list_sets[2]))
