from sys import stdin

line: str = stdin.readline().strip()
maximum: float = float("-inf")
coordinates: list = []

while line:
    coordinates.append(list(map(int, line.split(","))))
    line = stdin.readline().strip()


def calculate_area(point1: list, point2: list) -> int:
    return abs(point1[0] - point2[0] + 1) * abs(point1[1] - point2[1] + 1)


for i, point in enumerate(coordinates):
    for next_point in coordinates[i + 1 :]:
        area: int = calculate_area(point, next_point)
        if area > maximum:
            maximum = area

print(maximum)
