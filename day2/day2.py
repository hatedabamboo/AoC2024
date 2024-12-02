filename = "day2/day2task.txt"

safe_reports = 0


def is_increasing(lst: list[int]) -> bool:
    return all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))


def is_decreasing(lst: list[int]) -> bool:
    return all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))


def is_gradual(lst: list[int]) -> bool:
    difference = [lst[i + 1] - lst[i] for i in range(len(lst) - 1)]
    return all(abs(diff) <= 3 for diff in difference)


def is_popping_helps(lst: list[int]) -> bool:
    for i in range(len(lst)):
        list_to_iterate = lst[:i] + lst[i + 1 :]
        if is_increasing(list_to_iterate) or is_decreasing(list_to_iterate):
            if is_gradual(list_to_iterate):
                return True
    return False


with open(filename, "r", encoding="UTF-8") as file:
    while line := file.readline():
        lst = list(map(int, line.strip().split(" ")))
        if (is_increasing(lst) or is_decreasing(lst)) and is_gradual(lst):
            safe_reports += 1
        elif is_popping_helps(lst):
            safe_reports += 1

print(safe_reports)
