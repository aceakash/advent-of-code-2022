def input_lines(filename):
    with open('day2_input.txt') as fp:
        lines = [l.strip() for l in fp.readlines()]
    return lines

if __name__ == "__main__":
    lines = input_lines('day2_input.txt')

    total_score1 = 0
    lookup1 = {
        'A X': 1 + 3,
        'A Y': 2 + 6,
        'A Z': 3 + 0,
        'B X': 1 + 0,
        'B Y': 2 + 3,
        'B Z': 3 + 6,
        'C X': 1 + 6,
        'C Y': 2 + 0,
        'C Z': 3 + 3,
    }
    for line in lines:
        total_score1 += lookup1[line]
    
    assert total_score1 == 14531

    total_score2 = 0
    lookup2 = {
        'A X': 3 + 0,
        'A Y': 1 + 3,
        'A Z': 2 + 6,
        'B X': 1 + 0,
        'B Y': 2 + 3,
        'B Z': 3 + 6,
        'C X': 2 + 0,
        'C Y': 3 + 3,
        'C Z': 1 + 6,
    }
    for line in lines:
        total_score2 += lookup2[line]
    
    assert total_score2 == 11258