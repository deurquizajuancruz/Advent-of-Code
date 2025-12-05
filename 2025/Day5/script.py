import sys

total: int = 0

with open(sys.argv[1]) as f1, open(sys.argv[2]) as f2:
    ranges = f1.read().splitlines()
    numbers = f2.read().splitlines()

for number in numbers:
    is_in_range: bool = False
    int_number = int(number)
    for r in ranges:
        first, second = map(int, r.split("-"))
        if int_number >= first and int_number <= second:
            is_in_range = True
            total += 1
            break


print(total)
