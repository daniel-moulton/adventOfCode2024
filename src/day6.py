from pprint import pprint


def day6part1():
    with open("inputs/day6.txt") as f:
        lines = [list(line.strip()) for line in f.readlines()]
        count = 1  # starting point

        start_i, start_j = 0, 0
        for i in range(0, len(lines)):
            for j in range(0, len(lines[i])):
                if lines[i][j] == '^':
                    start_i, start_j = i, j
                    break

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left

        current_direciton = 0
        i, j = start_i, start_j
        while True:
            try:
                di, dj = directions[current_direciton]
                if (lines[i + di][j + dj] == '.'):
                    count += 1
                    lines[i + di][j + dj] = 'X'
                    i, j = i + di, j + dj
                elif lines[i + di][j + dj] == 'X' or lines[i + di][j + dj] == '^':
                    i, j = i + di, j + dj
                else:
                    current_direciton = (current_direciton + 1) % 4
            except IndexError:
                print(count)
                break
        
        pprint(lines)


day6part1()
