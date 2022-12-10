# returns (instr, increment, cycles_used)
def parse(line):
    instr = line.strip()
    if instr == 'noop':
        return ('noop', 0, 1)
    incr = int(instr.split(' ')[1])
    return ('addx', incr, 2)    

instrs = []
with open("day10_input.txt") as f:
    instrs = [parse(l) for l in f]

i = 0
cycle = 0
x = 1
waiting_to_addx = (False, 0, 0) # waiting, increment, source_cycle
sum = 0
while i < len(instrs):
    cycle += 1
    
    # this is where you measure the value of X
    print('======')
    print(f'Cycle {cycle} started')
    
    print(f'waiting_to_addx[0]: {waiting_to_addx[0]}')
    if waiting_to_addx[0]:
        print('entered if, ', waiting_to_addx[2] + 2)
        if waiting_to_addx[2] + 2 != cycle:
            print(f'x: {x}, cycle: {cycle}, signal strength: {x*cycle}')
            if cycle in [20, 60, 100, 140, 180, 220]:
                sum += x * cycle
            continue
        x += waiting_to_addx[1]
        waiting_to_addx = (False, 0, 0)
        i += 1

    if i >= len(instrs):
        break
    print(f'x: {x}, cycle: {cycle}, signal strength: {x*cycle}')
    if cycle in [20, 60, 100, 140, 180, 220]:
        sum += x * cycle
    instr = instrs[i]
    print(f'started processing instr: {instr}')
    if instr[0] == 'noop':
        i += 1 # instruction processed
        continue
    # instr is addx incr
    print('about to set waiting_to_addx to True')
    waiting_to_addx = (True, instr[1], cycle)
    

print(sum)

    # for l in f:
    #     print('--------')
    #     instr = l.strip()
    #     print(instr)
    #     cycle += 1
    #     print('1. cycle, x: ', cycle, x, cycle * x)
    #     if instr == 'noop':
    #         continue
    #     incr = int(instr.split(' ')[1])
    #     cycle += 1
    #     print('2. cycle, x: ', cycle, x, cycle * x)
    #     x += incr
    #     cycle += 1
    #     print('3. cycle, x: ', cycle, x, cycle * x)
    
    # print(x)

    
        
