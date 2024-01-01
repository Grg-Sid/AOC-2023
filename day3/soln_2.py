with open("./input.txt") as input_file:
    data = input_file.read().split("\n")

    ans = 0
    map = ""
    n = 0
    dict = {}
    ratio = []

    for word in data:
        n = max(len(word), n)
        map += word

    def gear_ratio(idx: int, x: int) -> int:
        if idx not in dict.keys():
            dict[idx] = int(x)
            return 0
        elif idx in dict.keys() and dict[idx] != int(x):
            dict[idx] = dict[idx] * int(x)
            return dict[idx]

    def is_symbol(idx: int):
        if idx % n == 0 or idx + 1 % n == 0 or idx < 0 or idx > len(map):
            return False
        if map[idx] != "." and not map[idx].isdigit():
            if map[idx] == "*":
                ratio.append(gear_ratio(idx, x))
            return True
        if map[idx + 1] != "." and not map[idx + 1].isdigit():
            if map[idx + 1] == "*":
                ratio.append(gear_ratio(idx + 1, x))
            return True
        if map[idx - 1] != "." and not map[idx - 1].isdigit():
            if map[idx - 1] == "*":
                ratio.append(gear_ratio(idx - 1, x))
            return True

        return False

    x = ""
    start = 0
    for i in range(0, len(map)):
        if map[i].isdigit():
            start = i
            x += map[i]
            continue

        elif x != "":
            start = i - len(x)

            for j in range(start, i):
                if is_symbol(j) or is_symbol(j + n) or is_symbol(j - n):
                    x = ""
                    break
            x = ""
    print(sum(ratio))
