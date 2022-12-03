def input_lines(filename):
    with open(filename) as fp:
        lines = [l.strip() for l in fp.readlines()]
    return lines

def priority(dupe):
    return 
    
if __name__ == "__main__":
    lines, total = input_lines('day3_input.txt'), 0
    for l in lines:
        half = len(l)//2
        compartment1, compartment2 = set(l[:half]), set(l[half:])
        dupe = list(compartment1.intersection(compartment2))[0]
        offset = 96 if 'a' <= dupe <= 'z' else 38
        total += ord(dupe) - offset

    print(total)


    
    