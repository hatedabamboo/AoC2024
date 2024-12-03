import re

filename = "day3/day3task.txt"
correct_mul = re.compile(r"mul\(\d{1,4}\,\d{1,4}\)")
mul_list = []

with open(filename, "r", encoding="UTF-8") as file:
    while line := file.readline():
        matches = correct_mul.findall(line)
        for match in matches:
            num1, num2 = match.split("(")[1].split(")")[0].split(",")
            mul_list.append(int(num1) * int(num2))

print(sum(mul_list))
