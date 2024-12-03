import re

filename = "day3/day3task.txt"

instruction_pattern = re.compile(r"do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)")
correct_mul = re.compile(r"mul\(\d{1,4}\,\d{1,4}\)")

mul_list_pt1, mul_list_pt2 = [], []

with open(filename, "r", encoding="UTF-8") as file:
    while line := file.readline():
        matches = correct_mul.findall(line)
        for match in matches:
            num1, num2 = match.split("(")[1].split(")")[0].split(",")
            mul_list_pt1.append(int(num1) * int(num2))

print(f"First part: {sum(mul_list_pt1)}")


with open(filename, "r", encoding="UTF-8") as file:
    mul_enabled = True
    for line in file:
        instructions = re.finditer(instruction_pattern, line)
        for instruction_match in instructions:
            instruction = instruction_match.group(0)
            if instruction == "do()":
                mul_enabled = True
            elif instruction == "don't()":
                mul_enabled = False
            elif "mul(" in instruction:
                if mul_enabled:
                    num1, num2 = map(
                        int, instruction.split("(")[1].split(")")[0].split(",")
                    )
                    mul_list_pt2.append(num1 * num2)

print(f"Second part: {sum(mul_list_pt2)}")
