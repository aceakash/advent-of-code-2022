def input_lines(filename):
    with open(filename) as fp:
        lines = [l.strip() for l in fp.readlines()]
    return lines

# 34-82,33-81
# 59-59,69-73
def parse(lines):
    ranges = []
    for l in lines:
        linerange = []
        pairs = l.split(',')
        for p in pairs:
            nums = tuple(p.split('-'))
            linerange.append(nums)
        ranges.append(linerange)
    return ranges

def part1(ranges):
    count = 0
    for r in ranges:
        # [a-b,c-d]
        a,b,c,d = r[0][0], r[0][1], r[1][0], r[1][1]
        
        if a <= c and d <= b:
            count += 1
            # print("first block: +1")
            print(f"one: {a}-{b}, {c}-{d}")
            continue
        if a >= c and d >= b:
            count += 1
            # print("second block: +1")
            print(f"two: {a}-{b}, {c}-{d}")
            continue
    return count

    
def part2(ranges):
    return None

if __name__ == "__main__":
    lines = input_lines('day4_input.txt')
    ranges = parse(lines)
    print(part1(ranges))

    # print(part2(lines))

    
    