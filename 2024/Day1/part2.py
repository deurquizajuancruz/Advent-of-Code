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
similarity: int = 0
for i in range(len(list1)):
    count: int = 0
    if list1[i] not in list2:
        continue
    number: int = list1[i]
    indice: int = list2.index(number)
    while number == list2[indice]:
        count += 1
        indice += 1
    similarity += number * count
print(f"The similarity score is {similarity}")
