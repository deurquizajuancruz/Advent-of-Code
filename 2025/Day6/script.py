import operator
from functools import reduce
from sys import stdin


def create_list(line: str) -> list:
    return list(map(int, list(filter(None, line.split(" ")))))


line: str = stdin.readline().strip()
first_numbers: list = create_list(line)
line = stdin.readline().strip()
second_numbers: list = create_list(line)
line = stdin.readline().strip()
third_numbers: list = create_list(line)
line = stdin.readline().strip()
fourth_numbers: list = create_list(line)
line = stdin.readline().strip()
operations: list = list(filter(None, line.split(" ")))

n: int = len(operations)
grand_total: int = 0
for number in range(n):
    numbers: list = [
        first_numbers[number],
        second_numbers[number],
        third_numbers[number],
        fourth_numbers[number],
    ]
    grand_total += (
        reduce(operator.mul, numbers)
        if operations[number] == "*"
        else reduce(operator.add, numbers)
    )

print(grand_total)
