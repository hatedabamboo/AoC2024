filename = "day1task.txt"

distances, left_list, right_list = [], [], []

with open(filename, "r", encoding="UTF-8") as file:
    while line := file.readline():
        num1, num2 = line.rstrip().split("  ")
        left_list.append(int(num1))
        right_list.append(int(num2))

left_list.sort(key=lambda x: x, reverse=False)
right_list.sort(key=lambda x: x, reverse=False)

for i, num in enumerate(left_list):
    distances.append(abs(num - right_list[i]))

print(sum((distances)))
