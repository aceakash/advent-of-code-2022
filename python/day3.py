def input_lines(filename):
    with open(filename) as fp:
        lines = [l.strip() for l in fp.readlines()]
    return lines

def priority(dupe):
    if 'a' <= dupe <= 'z':
        return ord(dupe) - 96
    if 'A' <= dupe <= 'Z':
        return ord(dupe) - 38

if __name__ == "__main__":
    lines = input_lines('day3_input.txt')
    tot = 0
    for l in lines:
        half = len(l)//2
        compartment1 = set(l[:half])
        compartment2 = set(l[half:])
        dupe = list(compartment1.intersection(compartment2))[0]
        tot += priority(dupe)

    print(tot)
    # print(priority('P'), ord('P'))

    
    