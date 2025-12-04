from sys import stdin

line = stdin.readline()
lines = line.split(",")
sum: int = 0
for range_numbers in lines:
    limits = range_numbers.split("-")
    first, second = int(limits[0]), int(limits[1])
    for i in range(first, second):
        i_string = str(i)
        if len(i_string) % 2 != 0:
            continue
        half: int = int(len(i_string) / 2)
        first_string, second_string = i_string[0:half], i_string[half : len(i_string)]
        if first_string == second_string:
            sum += i

print(sum)
