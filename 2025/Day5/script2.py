from sys import stdin

line:str = stdin.readline()
arr_ranges: list = []
while line:
    first, second = map(int, line.split("-"))
    arr_ranges.append([first, second])
    line = stdin.readline()


def clave(rango) -> int:
    return rango[0]


arr_ranges.sort(key=clave)
current_start, current_end = arr_ranges[0][0], arr_ranges[0][1]
total: int = 0
for ranges in arr_ranges[1:]:
    start, end = ranges[0], ranges[1]
    if start <= current_end + 1:
        current_end = max(current_end, end)
    else:
        total += current_end - current_start + 1
        current_start, current_end = start, end

total += current_end - current_start + 1
print(total)