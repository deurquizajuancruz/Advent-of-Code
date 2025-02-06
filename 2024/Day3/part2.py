import re
from sys import stdin

def sum_enabled_muls() -> int:
    mul_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    do_pattern = re.compile(r"do\(\)")
    dont_pattern = re.compile(r"don't\(\)")
    
    enabled: bool = True
    total: int = 0
    
    for match in re.finditer(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", text):
        instr = match.group()
        
        if do_pattern.fullmatch(instr):
            enabled = True
        elif dont_pattern.fullmatch(instr):
            enabled = False
        elif enabled:
                numbers = instr.split("(")[1].split(")")[0].split(",")
                total += int(numbers[0]) * int(numbers[1])
    
    return total

text = stdin.read()
print(sum_enabled_muls())
