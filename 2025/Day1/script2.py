from sys import stdin

point: int = 50
count: int = 0
line = stdin.readline()
while line:
    direction: str = line[0]
    number: int = int(line[1:])
    copy: int = point
    if direction == "L":
        for i in range(number):
            point -= 1
            if point < 0:
                point += 100
            if point == 0:
                count += 1
    else:
        for i in range(number):
            point += 1
            if point > 99:
                point -= 100
            if point == 0:
                count += 1
    line = stdin.readline()

print(count)
