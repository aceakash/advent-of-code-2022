with open("day4_input.txt") as f:
    part1, part2 = 0, 0
    for line in f:
        [[a,b], [c,d]] = map(lambda x: list(map(int, x)),
                            map(lambda x: x.split('-'), 
                                line.strip().split(',')))
        if (a <= c and d <= b) or (a >= c and d >= b):
            part1 += 1
        if not (b < c or d < a):
            part2 += 1
    print(part1, part2)
