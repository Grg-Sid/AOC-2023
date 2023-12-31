import re


def split_line(line) -> int:
    game = line.split(":")[1]

    dice = re.split(r"[,;]", game)

    red_count = 0
    blue_count = 0
    green_count = 0
    min_red = 0
    min_blue = 0
    min_green = 0
    for die in dice:
        die = die.strip()
        if "red" in die:
            red_count = [int(num) for num in die.split() if num.isdigit()][0]
            min_red = max(min_red, red_count)
        elif "blue" in die:
            blue_count = [int(num) for num in die.split() if num.isdigit()][0]
            min_blue = max(min_blue, blue_count)
        else:
            green_count = [int(num) for num in die.split() if num.isdigit()][0]
            min_green = max(min_green, green_count)
    return min_red * min_blue * min_green


with open("./input.txt") as input_file:
    ans = 0
    data = input_file.read().splitlines()
    for id, line in zip(range(len(data)), data):
        ans += split_line(line)
    print(ans)
