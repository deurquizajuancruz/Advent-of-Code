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
        distancec: float = calculate_distance(coordinate, compare_coordinates)
        second_index += 1
        all_distances.append(
            (
                distancec,
                index - 1,
                second_index - 1,
                coordinate[0],
                compare_coordinates[0],
            )
        )

    index += 1

all_distances = sorted(all_distances, key=lambda x: x[0])

list_sets: list = []


def what_circuit(index: int) -> set | None:
    for set in list_sets:
        if index in set:
            return set
    return None


last1, last2 = 0, 0
for distance in all_distances:
    circuit1: set | None = what_circuit(distance[1])
    circuit2: set | None = what_circuit(distance[2])
    if not circuit1 and not circuit2:
        list_sets.append(set((distance[1], distance[2])))
    elif circuit1 and not circuit2:
        circuit1.add(distance[2])
    elif circuit2 and not circuit1:
        circuit2.add(distance[1])
    elif circuit1 != circuit2:
        circuit1.update(circuit2)  # type: ignore
        list_sets.remove(circuit2)
    if len(list_sets) == 1:
        if len(list_sets[0]) == 1000:
            last1 = distance[3]
            last2 = distance[4]
            break

print(last1 * last2)
