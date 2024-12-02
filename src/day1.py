def day1part1():
    
    with open('inputs/day1.txt') as f:
        lines = f.readlines()

    nums1, nums2 = [], []

    diff = 0

    for i in range(len(lines)):
        num1, num2 = lines[i].strip().split()
        num1, num2 = int(num1), int(num2)

        nums1.append(num1)
        nums2.append(num2)

    nums1 = sorted(nums1)
    nums2 = sorted(nums2)

    for i in range(len(nums1)):
        diff += abs(nums1[i] - nums2[i])
    
    print(diff)

def day1part2():
    with open('inputs/day1.txt') as f:
        lines = f.readlines()
    
    nums1, nums2 = [], []

    similiarity_score = 0

    scores = {}

    for i in range(len(lines)):
        num1, num2 = lines[i].strip().split()
        num1, num2 = int(num1), int(num2)

        nums1.append(num1)
        nums2.append(num2)
    
    for i in range(len(nums1)):
        if scores.get(nums1[i]) is None:
            scores[nums1[i]] = nums2.count(nums1[i])
            print(nums2.count(nums1[i]))
        similiarity_score += scores[nums1[i]] * nums1[i]
    
    print("\n")
    print(similiarity_score)



day1part1()
day1part2()
