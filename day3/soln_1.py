with open("./input.txt") as input_file:
    ans = 0
    data = input_file.read().split("\n")

    map = ""
    n = 0
    for word in data:
        n = max(len(word), n)
        map += word

    def is_symbol(idx: int):
        if idx % n == 0 or idx + 1 % n == 0 or idx < 0 or idx > len(map):
            return False
        if map[idx] != "." and not map[idx].isdigit():
            return True
        if map[idx + 1] != "." and not map[idx + 1].isdigit():
            return True
        if map[idx - 1] != "." and not map[idx - 1].isdigit():
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
                    if int(x) > 999:
                        print(x)
                    ans += int(x)
                    x = ""
                    break
            x = ""

    print(ans)
