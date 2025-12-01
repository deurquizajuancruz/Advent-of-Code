from sys import stdin

point: int = 50
count: int = 0
line = stdin.readline()
while line:
    direction: str = line[0]
    number: int = int(line[1:])
    if direction == "L":
        point -= number
        while point < 0:
            point += 100
    else:
        point += number
        while point > 99:
            point -= 100
    if point == 0:
        count +=1
    line = stdin.readline()

print(count)
