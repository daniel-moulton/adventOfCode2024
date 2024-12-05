def day4part1():
    lines = []
    count = 0
    substr = "XMAS"
    with open("inputs/day4.txt") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            # Check for horizontal matches
            if j + len(substr) <= len(lines[0]):
                if lines[i][j:j+len(substr)] == substr or lines[i][j:j+len(substr)] == substr[::-1]:
                    count += 1

            # Check for vertical matches
            if i + len(substr) <= len(lines):
                temp = ""
                for k in range(len(substr)):
                    temp += lines[i+k][j]
                if temp == substr or temp == substr[::-1]:
                    count += 1

            # Check for diagonal matches
            if i + len(substr) <= len(lines):
                temp_right = ""
                temp_left = ""
                try:
                    for k in range(len(substr)):
                        if j+k < len(lines[0]):
                            temp_right += lines[i+k][j+k]
                        if j-k >= 0:
                            temp_left += lines[i+k][j-k]
                    if temp_right == substr or temp_right == substr[::-1]:
                        count += 1
                    if temp_left == substr or temp_left == substr[::-1]:
                        count += 1
                except IndexError:
                    pass

    print(count)


def day4part2():
    lines = []
    count = 0

    target_sum = 2*ord("M") + 2*ord("S")
    target_mult = ord("M") * ord("S")

    with open("inputs/day4.txt") as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] != "A":
                continue
            # Logic here is if we need a cross of MAS then we'll have two Ms and two Ss.
            # Checking both the sum of the corners as well as the product of the diagonals.
            # Having just one i.e. the sum could lead to cases where we have four letters who also sum to the same value.
            # Checking the product ensures the diagonals are opposites i.e. to avoid SAS and MAM.
            try:
                tl, tr, bl, br = lines[i-1][j-1], lines[i-1][j+1], lines[i+1][j-1], lines[i+1][j+1]
                if ord(tl) + ord(tr) + ord(bl) + ord(br) == target_sum and ord(tl) * ord(br) == target_mult:
                    print(i, j)
                    print(tl, tr, bl, br)
                    print("\n")
                    count += 1
            except IndexError:
                pass

    print(count)


day4part1()
day4part2()
