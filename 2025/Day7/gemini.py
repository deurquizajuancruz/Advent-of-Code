from sys import stdin


def solve():
    s_line = stdin.readline().strip()

    width = len(s_line)

    previous_line = [0] * width
    start_index = s_line.find("S")

    previous_line[start_index] = 1

    line = stdin.readline().strip()

    while line:
        new_line = [0] * width

        for i in range(width):
            if previous_line[i] == 0:
                continue

            if line[i] == "^":
                new_line[i - 1] += previous_line[i]
                new_line[i + 1] += previous_line[i]
            else:
                new_line[i] += previous_line[i]

        previous_line = new_line

        line = stdin.readline().strip()

    print(sum(previous_line))


if __name__ == "__main__":
    solve()
