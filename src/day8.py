import math


def day8part1():
    with open("inputs/day8.txt") as f:
        lines = [line.strip() for line in f.readlines()]

        max_i = len(lines)
        max_j = len(lines[0])

        char_positions = {}
        antinode_positions = set()

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char != ".":
                    if char not in char_positions:
                        char_positions[char] = []
                    char_positions[char].append((i, j))

        for char in char_positions:
            for i in range(len(char_positions[char])):
                for j in range(i + 1, len(char_positions[char])):
                    pos1 = char_positions[char][i]
                    pos2 = char_positions[char][j]
                    distance_between = distance(pos1, pos2)

                    antinode_pos1, antinode_pos2 = calculate_antinodes(pos1, pos2, distance_between)

                    for pos in [antinode_pos1, antinode_pos2]:
                        if pos[0] >= 0 and pos[0] < max_i and pos[1] >= 0 and pos[1] < max_j:
                            antinode_positions.add(pos)

        print(len(antinode_positions))


def distance(pos1, pos2):
    # Manhattan distance betwen two points
    return ((pos1[0] - pos2[0]), (pos1[1] - pos2[1]))


def calculate_antinodes(pos1, pos2, distance):
    antinode_pos1 = (pos1[0] + distance[0], pos1[1] + distance[1])
    antinode_pos2 = (pos2[0] - distance[0], pos2[1] - distance[1])
    return antinode_pos1, antinode_pos2


def day8part2():
    with open("inputs/day8.txt") as f:
        lines = [line.strip() for line in f.readlines()]

        max_i = len(lines)
        max_j = len(lines[0])

        char_positions = {}
        antinode_positions = set()

        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char != ".":
                    if char not in char_positions:
                        char_positions[char] = []
                    char_positions[char].append((i, j))

        for char in char_positions:
            for i in range(len(char_positions[char])):
                for j in range(i + 1, len(char_positions[char])):
                    pos1 = char_positions[char][i]
                    pos2 = char_positions[char][j]
                    distance_between = distance(pos1, pos2)
                    # Simplifies to the smallest possible integer values for
                    # the ratio (gradient)
                    distance_between = simplify_distance(distance_between)

                    antinodes = calculate_v2_antinodes(pos1, pos2, distance_between, max_i, max_j)
                    antinode_positions.update(antinodes)

        with open("out2.txt", "w") as f:
            f.write("\n".join([f"{x[0]} {x[1]}" for x in antinode_positions]))
        print(len(antinode_positions))


def calculate_v2_antinodes(pos1, pos2, distance, max_i, max_j):
    valid = True
    antinode_pos1 = pos1
    antinodes = set()
    while valid:
        antinode_pos = (antinode_pos1[0] + distance[0], antinode_pos1[1] + distance[1])
        if antinode_pos == (0,9):
            print("here")
        if is_valid_point(antinode_pos, max_i, max_j):
            antinodes.add(antinode_pos)
            antinode_pos1 = antinode_pos
        else:
            valid = False

    antinode_pos2 = pos2
    valid = True
    while valid:
        if antinode_pos2 == (0, 9):
            print("here2")
        antinode_pos = (antinode_pos2[0] - distance[0], antinode_pos2[1] - distance[1])
        if is_valid_point(antinode_pos, max_i, max_j):
            antinodes.add(antinode_pos)
            antinode_pos2 = antinode_pos
        else:
            valid = False

    antinodes.add(pos1)
    antinodes.add(pos2)

    return antinodes


def is_valid_point(pos, max_i, max_j):
    return pos[0] >= 0 and pos[0] < max_i and pos[1] >= 0 and pos[1] < max_j


def simplify_distance(distance):
    # Simplify the ratio of the distance between two points
    # to the smallest possible integer values
    x, y = distance
    gcd = math.gcd(x, y)
    return (x // gcd, y // gcd)


day8part1()
day8part2()
