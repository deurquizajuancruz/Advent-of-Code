from sys import stdin

line = stdin.readline()
lines = line.split(",")
total: int = 0
for range_numbers in lines:
    limits = range_numbers.split("-")
    first, second = int(limits[0]), int(limits[1])
    for i in range(first, second + 1):
        i_string: str = str(i)
        i_double: str = i_string * 2
        cut: str = i_double[1 : len(i_double) - 1]
        if i_string in cut:
            total+= i


print(total)
