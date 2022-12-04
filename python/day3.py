def input_lines(filename):
    with open(filename) as fp:
        lines = [l.strip() for l in fp.readlines()]
    return lines

def priority(item):
    return ord(item) - (96 if 'a' <= item <= 'z' else 38)

def part1(lines):
    total = 0
    for l in lines:
        half = len(l)//2
        compartment1, compartment2 = set(l[:half]), set(l[half:])
        dupe = list(compartment1.intersection(compartment2))[0]
        total += priority(dupe)
    return total
    
def part2(lines):
    total, i = 0, 0 
    while i < len(lines):
        common = set(lines[i]).intersection(set(lines[i+1])).intersection(set(lines[i+2]))
        total += priority(list(common)[0])
        i+=3
    return total

if __name__ == "__main__":
    lines = input_lines('day3_input.txt')
    print(part1(lines))

    print(part2(lines))

    
    