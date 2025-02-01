from sys import stdin


def check_removing(arrayNumber: list) -> bool:
    for remove_position in range(len(arrayNumber)):
        removed: int = arrayNumber.pop(remove_position)
        is_safe: bool = all(
            arrayNumber[i] < arrayNumber[i + 1] for i in range(len(arrayNumber) - 1)
        ) or all(
            arrayNumber[i] > arrayNumber[i + 1] for i in range(len(arrayNumber) - 1)
        )
        i: int = 0
        while i < len(arrayNumber) - 1 and is_safe:
            difference: int = abs(arrayNumber[i] - arrayNumber[i + 1])
            if difference < 1 or difference > 3:
                is_safe = False
            i += 1
        if is_safe:
            return True
        arrayNumber.insert(remove_position, removed)
    return False


count: int = 0
report: str = stdin.readline()
while report:
    report = report.split()
    arrayNumber: list = [int(string) for string in report]
    i: int = 0
    is_safe: bool = all(
        arrayNumber[i] <= arrayNumber[i + 1] for i in range(len(arrayNumber) - 1)
    ) or all(arrayNumber[i] >= arrayNumber[i + 1] for i in range(len(arrayNumber) - 1))
    while i < len(arrayNumber) - 1 and is_safe:
        difference: int = abs(arrayNumber[i] - arrayNumber[i + 1])
        if difference < 1 or difference > 3:
            is_safe = False
        i += 1
    if is_safe:
        count += 1
    else:
        if check_removing(arrayNumber):
            count += 1
    report = stdin.readline()
print(f"The count is: {count}")
