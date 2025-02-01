from sys import stdin

list1: list = []
list2: list = []
line = stdin.readline()
while line:
    line = line.split()
    list1.append(int(line[0]))
    list2.append(int(line[1]))
    line = stdin.readline()

list1.sort()
list2.sort()
difference: int = 0
for i in range(len(list1)):
    difference += abs(list1[i] - list2[i])
print(difference)
