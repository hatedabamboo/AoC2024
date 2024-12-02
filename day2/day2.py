filename = "day2/day2task.txt"

safe_reports = 0

with open(filename, "r", encoding="UTF-8") as file:
    while line := file.readline():
        lst = list(map(int, line.strip().split(' ')))
        if all(lst[i] < lst[i+1] for i in range(len(lst) -1)): # increasing
            difference = [lst[i+1] - lst[i] for i in range(len(lst) - 1)]
            if all(abs(diff) <= 3 for diff in difference):
                safe_reports += 1
        elif all(lst[i+1] < lst[i] for i in range(len(lst) -1)): # increasing
            difference = [lst[i] - lst[i+1] for i in range(len(lst) - 1)]
            if all(diff <= 3 for diff in difference):
                safe_reports += 1
        else:
            continue

print(safe_reports)
