from sys import stdin

diccionario: dict = {}
dicc_z: dict = {}
lineas_input: list = []

line: str = stdin.readline().strip()
while line != "":
    array: list = line.split()
    diccionario[array[0][:-1]] = int(array[1])
    line = stdin.readline().strip()

line = stdin.readline().strip()
while line:
    lineas_input.append(line)
    line = stdin.readline().strip()

index: int = 0
while True:
    delete_line: list = []
    for line in lineas_input:
        new_line: list = line.split()
        if new_line[0] not in diccionario or new_line[2] not in diccionario:
            continue
        result: int = 0
        operation: str = new_line[1]
        if operation == "AND":
            result = diccionario[new_line[0]] & diccionario[new_line[2]]
        elif operation == "OR":
            result = diccionario[new_line[0]] | diccionario[new_line[2]]
        else:
            result = diccionario[new_line[0]] ^ diccionario[new_line[2]]
        if new_line[4][0] == "z":
            dicc_z[new_line[4]] = result
        else:
            diccionario[new_line[4]] = result
        delete_line.append(line)

    for eliminar in delete_line:
        if eliminar in lineas_input:
            lineas_input.remove(eliminar)

    if len(lineas_input) == 0:
        break

ordered_dict = dict(sorted(dicc_z.items(), key=lambda x: int(x[0][1:]), reverse=True))
final_number: str = ""
for key in ordered_dict.values():
    final_number += str(key)
print(f"Final number: {int(final_number, 2)}")
