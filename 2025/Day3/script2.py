from sys import stdin

line = stdin.readline().strip()
total = 0

while line:
    max_substring: int = 12
    max_number: str = ""
    start: int = 0

    for i in range(max_substring):
        remaining: int = max_substring - len(max_number)
        end: int = len(line) - remaining + 1
        best_digit: str = "-1"
        best_index: int = -1

        for k in range(start, end):
            if line[k] > best_digit:
                best_digit = line[k]
                best_index = k

        max_number += best_digit
        start = best_index + 1

    total += int(max_number)
    line = stdin.readline().strip()

print(total)
