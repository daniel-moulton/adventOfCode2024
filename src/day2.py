def day2part1():
    safe = 0
    with open('inputs/day2.txt') as f:
        lines = f.readlines()
        for line in lines:
            nums = line.split()
            nums = [int(num) for num in nums]

            direction = -1 if nums[1] - nums[0] < 0 else 1

            for i in range(1, len(nums)):
                if abs(nums[i] - nums[i-1]) < 1 or abs(nums[i] - nums[i-1]) > 3:
                    break
                if (direction * (nums[i] - nums[i-1]) < 0):
                    break
            else:
                safe += 1
                print(nums)
        
    print(safe)

def day2part2():
    safe = 0
    with open('inputs/day2.txt') as f:
        lines = f.readlines()
        for line in lines:
            nums = line.split()
            nums = [int(num) for num in nums]

            direction = -1 if nums[1] - nums[0] < 0 else 1

            single_catch = False

            for i in range(1, len(nums)):
                if abs(nums[i] - nums[i-1]) < 1 or abs(nums[i] - nums[i-1]) > 3:
                    if single_catch:
                        break
                    else:
                        single_catch = True
                if (direction * (nums[i] - nums[i-1]) < 0):
                    if single_catch:
                        break
                    else:
                        single_catch = True
            else:
                safe += 1
                print(nums)
        
    print(safe)

day2part1()
day2part2()
