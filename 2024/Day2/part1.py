from sys import stdin

count: int = 0
report: str = stdin.readline()
while report:
    report = report.split()
    arrayNumber: list = [int(string) for string in report]
    i: int = 0
    isSafe: bool = all(
        arrayNumber[i] <= arrayNumber[i + 1] for i in range(len(arrayNumber) - 1)
    ) or all(arrayNumber[i] >= arrayNumber[i + 1] for i in range(len(arrayNumber) - 1))
    while i < len(arrayNumber) - 1 and isSafe:
        difference: int = abs(arrayNumber[i] - arrayNumber[i + 1])
        if difference < 1 or difference > 3:
            isSafe = False
        i += 1
    if isSafe:
        count += 1
    report = stdin.readline()
print(f" The count is: {count}")
