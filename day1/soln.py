NUMS = ["nine", "eight", "seven", "six", "five", "four", "three", "two", "one", "zero"]
NUMERICALS = ["9", "8", "7", "6", "5", "4", "3", "2", "1"]


def first_number(string: str) -> str:
    for i in range(len(string)):
        if string[i] in NUMERICALS:
            return string[i]
        else:
            for number, value in zip(NUMS, NUMERICALS):
                if string[i:].startswith(number):
                    return value


def last_number(string: str) -> str:
    for i in range(len(string) - 1, -1, -1):
        if string[i] in NUMERICALS:
            return string[i]
        else:
            for number, value in zip(NUMS, NUMERICALS):
                if string[i:].startswith(number):
                    return value


with open("./input.txt") as input_file:
    ans = 0
    data = input_file.read().splitlines()
    for line in data:
        number = first_number(line) + last_number(line)
        ans += int(number)
    print(ans)
