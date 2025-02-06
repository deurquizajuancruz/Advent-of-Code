from sys import stdin


def mul(number1: int, number2: int) -> int:
    return number1 * number2


text: str = stdin.read()
total: int = 0
while text:
    index: int = text.find("mul")
    if index == -1:
        break
    text = text[index:]
    if text[3] == "(":
        index_end: int = text.find(")")
        index_comma: int = text.find(",")
        if index_end == -1 or index_comma == -1:
            continue
        if index_comma < index_end:
            numbers: list = text[4:index_end].split(",")
            if len(numbers) == 2:
                try:
                    number1, number2 = int(numbers[0]), int(numbers[1])
                    total += mul(number1, number2)
                except ValueError:
                    pass
    text = text[1:]
print(f"Result of adding up all the multiplications: {total}")
