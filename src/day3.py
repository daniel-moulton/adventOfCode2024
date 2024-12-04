import re


def day3part1():
    total = 0
    with open("inputs/day3.txt") as f:
        lines = f.readlines()
        # Find all matches in the line that match the regex "mul\([0-9]+,[0-9]+\)"
        for line in lines:
            matches = re.findall(r"mul\([0-9]+,[0-9]+\)", line)
            for match in matches:
                # Split the match into two numbers
                nums = match[4:-1].split(",")
                total += int(nums[0]) * int(nums[1])

    print(total)


def day3part2():
    total = 0
    with open("inputs/day3.txt") as f:
        lines = f.read()
        matches = list(re.finditer(r"mul\([0-9]+,[0-9]+\)", lines))
        dos = list(re.finditer(r"do\(\)", lines))
        donts = list(re.finditer(r"don't\(\)", lines))

        all_matches = sorted(
            [(match.start(), match.group()) for match in matches] +
            [(do.start(), do.group()) for do in dos] +
            [(dont.start(), dont.group()) for dont in donts],
            key=lambda x: x[0]
        )

        activated = True

        for i in range(len(all_matches)):
            if all_matches[i][1] == "do()":
                activated = True
            elif all_matches[i][1] == "don't()":
                activated = False
            elif activated:
                nums = all_matches[i][1][4:-1].split(",")
                total += int(nums[0]) * int(nums[1])
        
    print(total)

day3part1()
day3part2()
