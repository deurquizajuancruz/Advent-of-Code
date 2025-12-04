from sys import stdin

line: str = stdin.readline().strip()
last_row_number: int = 0
last_position_row: int = len(line)
matrix: list = []
while line:
    matrix.append(list(line))
    last_row_number += 1
    line = stdin.readline().strip()


def check_adjacent_special_line(my_line: list, adjacent_line: list, index: int) -> int:
    return str(
        my_line[index - 1]
        + my_line[index + 1]
        + adjacent_line[index]
        + adjacent_line[index - 1]
        + adjacent_line[index + 1]
    ).count("@")


def check_adjacent(my_line: list, up_line: list, down_line: list, index: int) -> int:
    return str(
        my_line[index - 1]
        + my_line[index + 1]
        + up_line[index - 1]
        + up_line[index + 1]
        + up_line[index]
        + down_line[index - 1]
        + down_line[index + 1]
        + down_line[index]
    ).count("@")


def corner_left(my_line: list, up_line: list, down_line: list, index: int) -> int:
    return str(
        my_line[index + 1]
        + up_line[index + 1]
        + up_line[index]
        + down_line[index + 1]
        + down_line[index]
    ).count("@")


def corner_right(my_line: list, up_line: list, down_line: list, index: int) -> int:
    return str(
        my_line[index - 1]
        + up_line[index - 1]
        + up_line[index]
        + down_line[index - 1]
        + down_line[index]
    ).count("@")


total: int = 0
keep_going: bool = True
while keep_going:
    keep_going = False
    replace: dict = {}
    number_line: int = -1   
    for line in matrix:
        number_line += 1
        indexes = []
        for index, char in enumerate(line):
            if char == ".":
                continue
            amount: int = 5
            if number_line == 0 or number_line + 1 == last_row_number:
                if index == 0 or index + 1 == last_position_row:
                    indexes.append(index)
                    total += 1
                elif number_line == 0:
                    amount = check_adjacent_special_line(matrix[0], matrix[1], index)
                else:
                    amount = check_adjacent_special_line(
                        matrix[last_row_number - 1], matrix[last_row_number - 2], index
                    )
            else:
                if index == 0:
                    amount = corner_left(
                        matrix[number_line],
                        matrix[number_line - 1],
                        matrix[number_line + 1],
                        index,
                    )
                elif index + 1 == last_position_row:
                    amount = corner_right(
                        matrix[number_line],
                        matrix[number_line - 1],
                        matrix[number_line + 1],
                        index,
                    )
                else:
                    # print(f"Linea {number_line} index {index}")
                    amount = check_adjacent(
                        matrix[number_line],
                        matrix[number_line - 1],
                        matrix[number_line + 1],
                        index,
                    )
            if amount < 4:
                keep_going = True
                indexes.append(index)
                total += 1
        replace[number_line] = indexes
    for index, line in enumerate(matrix):
        if index in replace.keys():
            replace_indexes: list = replace[index]
            line_list = list(line)
            for index_char in replace_indexes:
                line_list[index_char] = "."
            matrix[index] = line_list
    # for line in matrix:
    #     print(line)

print(total)
