with open("day5_input.txt") as f:
    stacks = [list(x) for x in [
        'RGJBTVZ',
        'JRVL',
        'SQF',
        'ZHNLFVQG',
        'RQTJCSMW',
        'SWTCHF',
        'DZCVFNJ',
        'LGZDWRFQ',
        'JBWVP'
    ]]
    i, count = -1, 0
    for line in f:
        i += 1
        if i < 10:
            continue
        split = line.split(' ')
        count, src, dst = int(split[1]), int(split[3]), int(split[5])
        
        ## part 1
        # for j in range(count):
        #     num = stacks[src-1].pop()
        #     stacks[dst-1].append(num)

        ## part 2
        move_start_idx = len(stacks[src-1])-count
        stacks[dst-1].extend(stacks[src-1][move_start_idx:])
        stacks[src-1] = stacks[src-1][:move_start_idx]
        
    str = ''
    for i in range(len(stacks)):
        str += stacks[i][-1] if len(stacks[i]) > 0 else ''
    print(str)

    
