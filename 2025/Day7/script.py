from sys import stdin
import re

count: int = 0
indexes: list = []

s_line: str = stdin.readline()
indexes.append(s_line.find("S"))
second_line: list = list(stdin.readline())
second_line[indexes[0]] = "|"
previous_line: str = "".join(second_line)
line: str = stdin.readline()

while line:
    new_line: str = line
    indexes = [match.start() for match in re.finditer(r"\|", previous_line)]
    for index in indexes:
        if new_line[index] == "^":
            new_line = new_line[: index - 1] + "|" + new_line[index:]
            new_line = new_line[: index + 1] + "|" + new_line[index + 2 :]
            count += 1
        else:
            new_line = new_line[:index] + "|" + new_line[index + 1 :]

    previous_line = new_line
    line = stdin.readline()

print(count)
