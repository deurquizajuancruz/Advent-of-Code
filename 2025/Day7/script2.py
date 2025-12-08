from sys import stdin
import re

indexes: list = []


def print_as_string(lista: list):
    print("".join(map(str, lista)))


s_line: str = stdin.readline().strip()
indexes.append(s_line.find("S"))
second_line: list = list(stdin.readline().strip())
second_line = [0] * len(s_line)
second_line[indexes[0]] = 1
previous_line: list = second_line
line: str = stdin.readline().strip()

# print(s_line)
# print_as_string(previous_line)

while line:
    new_line: list = [0] * len(line)
    indexes = [i for i, x in enumerate(previous_line) if x > 0]
    for index in indexes:
        if line[index] == "^":
            new_line[index] = 0
            new_line[index - 1] += previous_line[index]
            new_line[index + 1] += previous_line[index]
        else:
            new_line[index] += previous_line[index]

    # print_as_string(new_line)
    previous_line = new_line
    line = stdin.readline().strip()

print(sum(previous_line))
