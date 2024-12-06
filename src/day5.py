def day5part1():
    with open("inputs/day5.txt") as f:
        rules = {}

        sum = 0

        while True:
            line = f.readline().strip()
            if not line:
                break

            rule, value = int(line.split("|")[0]), int(line.split("|")[1])

            rules.setdefault(rule, set()).add(value)

        while True:
            line = f.readline().strip()

            if not line:
                break

            nums = list(map(int, line.split(",")))
            length = len(nums)
            for i, num in enumerate(nums):
                if i+1 == length:
                    continue
                if not rules.get(num):
                    break
                if nums[i+1] not in rules[num]:
                    break
            else:
                sum += nums[length//2]

        print(sum)


def day5part2():
    with open("inputs/day5.txt") as f:
        rules = {}

        sum = 0

        while True:
            line = f.readline().strip()
            if not line:
                break

            rule, value = int(line.split("|")[0]), int(line.split("|")[1])

            rules.setdefault(rule, set()).add(value)

        while True:
            line = f.readline().strip()

            if not line:
                break

            nums = list(map(int, line.split(",")))
            length = len(nums)
            loop = True
            fixed = False
            loops = 0
            while loop:
                loops += 1
                loop = False
                fixed = False
                for i, num in enumerate(nums):
                    if i+1 == length:
                        continue
                    if not rules.get(num) or nums[i+1] not in rules[num]:
                        fixed = True
                        nums[i], nums[i+1] = nums[i+1], nums[i]
                else:
                    if fixed:
                        loop = True
                    else:
                        break
            if loops > 1:
                sum += nums[length//2]

        print(sum)


day5part1()
day5part2()
