from sys import stdin

line: str = stdin.readline()
sum: int = 0
while line:
    max1: int = -1
    pos: int = -1
    for index, number in enumerate(line):
        if number == "\n":
            continue
        if int(number) > max1:
            max1 = int(number)
            pos = index
    max2: int = -1
    if pos + 2 == len(line):
        max2 = max1
        max1 = -1
        for number in line[0:pos]:
            if int(number) > max1:
                max1 = int(number)
    else:
        line = line[pos + 1 :]
        for number in line:
            if number == "\n":
                continue
            if int(number) > max2:
                max2 = int(number)
    max_number = str(max1) + str(max2)
    sum += int(max_number)
    line = stdin.readline()


print(sum)
