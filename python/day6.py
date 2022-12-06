with open("day6_input.txt") as f:
    a, i  = f.read(), 0
    # SEQ_LEN = 4  # part 1
    SEQ_LEN = 14  # part 2
    while True:
        sub = a[i:i+SEQ_LEN]
        if len(set(sub)) == SEQ_LEN:
            print(i+SEQ_LEN)
            break
        i += 1