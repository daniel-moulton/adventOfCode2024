import math


def day7part1():
    with open("inputs/day7.txt") as f:
        lines = [line.strip() for line in f.readlines()]

        count = 0

        for line in lines:
            target = int(line.split(":")[0])
            nums = [int(x) for x in line.split(" ")[1:]]

            if dfs(nums, target, []):
                count += target

        print(count)


def dfs(nums, target, ops):
    if math.prod(nums) == target or sum(nums) == target:
        return True

    while not (evaluate(nums, ops) == target and len(ops) == len(nums) - 1):
        if evaluate(nums, ops) < target or (evaluate(nums, ops) == target and len(ops) < len(nums) - 1):
            if len(ops) < len(nums) - 1:
                ops.append("*")
            else:
                if len(set(ops)) == 1 and ops[0] == "+":
                    return False
                else:
                    try:
                        num_times = 1
                        while ops.pop() != "*":
                            num_times += 1
                            pass
                        ops.append("+")
                    except IndexError:
                        return False
        elif evaluate(nums, ops) == target:
            if len(ops) == len(nums) - 1:
                return True
        elif evaluate(nums, ops) > target:
            try:
                num_times = 1
                while ops.pop() != "*":
                    num_times += 1
                    pass
                ops.append("+")
            except IndexError:
                return False
    return True


def evaluate(nums, ops):
    result = nums[0]
    for i in range(1, len(nums)):
        if i > len(ops):
            break
        if ops[i - 1] == "+":
            result += nums[i]
        elif ops[i - 1] == "*":
            result *= nums[i]
    return result


def day7part2():
    # Initially didn't want to have to do a fully exhaustive search as felt 
    # there were optimisations that could be made but for part 2 having an extra
    # operation would make that more difficul thatn it's worth.
    with open("inputs/day7.txt") as f:
        lines = [line.strip() for line in f.readlines()]

        count = 0

        for line in lines:
            target = int(line.split(":")[0])
            nums = [int(x) for x in line.split(" ")[1:]]

            if dfs_v2(nums, target, [], 0):
                count += target

        print(count)


def dfs_v2(nums, target, ops, index):
    if index == len(nums):
        return evaluate_v2(nums, ops) == target

    if dfs_v2(nums, target, ops + ["+"], index + 1):
        return True

    if dfs_v2(nums, target, ops + ["*"], index + 1):
        return True

    if dfs_v2(nums, target, ops + ["|"], index+1):
        return True

    return False


def evaluate_v2(nums, ops):
    result = nums[0]
    for i in range(1, len(nums)):
        if i > len(ops):
            break
        if ops[i - 1] == "+":
            result += nums[i]
        elif ops[i - 1] == "*":
            result *= nums[i]
        elif ops[i - 1] == "|":
            result = int(str(result) + str(nums[i]))
    return result



day7part1()
day7part2()