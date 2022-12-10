NOOP = 'noop'
ADDX = 'addx'

def parse(line):
    instr = line.strip()
    if instr == NOOP:
        return (NOOP, 0)
    return (ADDX, int(instr.split(' ')[1]))    

def render(cycle, x, lines):
    pixel = '#' if x%40 - 1 <= (cycle-1) % 40 <= x%40 + 1 else '.'
    lines.append(pixel)
        
def draw(lines):
    for j in range(6):
        for i in range(40):
            print(lines[40*j + i], end='')
        print('')


instrs = []
with open("day10_input.txt") as f:
    instrs = [parse(l) for l in f]

i, cycle, sum = 0, 0, 0
x = 1
waiting_to_addx = (False, 0, 0) # waiting, increment, source_cycle
lines = []
while i < len(instrs):
    cycle += 1
    if waiting_to_addx[0]:
        if waiting_to_addx[2] + 2 != cycle:
            render(cycle, x, lines)
            if cycle in [20, 60, 100, 140, 180, 220]:
                sum += x * cycle
            continue
        x += waiting_to_addx[1]
        waiting_to_addx = (False, 0, 0)
        i += 1

    if i >= len(instrs):
        break
    
    render(cycle, x, lines)
    if cycle in [20, 60, 100, 140, 180, 220]:
        sum += x * cycle
    instr = instrs[i]
    if instr[0] == NOOP:
        i += 1
        continue
    waiting_to_addx = (True, instr[1], cycle)
    
print(sum)
draw(lines)
