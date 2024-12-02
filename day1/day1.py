filename = "day1task.txt"

distances, left_list, right_list, occurences = [], [], [], []

with open(filename, "r", encoding="UTF-8") as file:
    while line := file.readline():
        num1, num2 = line.rstrip().split("  ")
        left_list.append(int(num1))
        right_list.append(int(num2))

left_list.sort(key=lambda x: x, reverse=False)
right_list.sort(key=lambda x: x, reverse=False)

for i, num in enumerate(left_list):
    distances.append(abs(num - right_list[i]))


occurence = {num: right_list.count(num) for num in left_list}

for k, v in occurence.items():
    occurences.append(k * v)

print(
    f"""Distance between points: {sum(distances)}
Sum of repetitions: {sum(occurences)}"""
)
