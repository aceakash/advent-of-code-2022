def input_lines(filename):
    with open('day2_input.txt') as fp:
        lines = [l.strip() for l in fp.readlines()]
    return lines

def parse_input1(lines):
    opponent_mapping = {'A': 'r', 'B': 'p', 'C': 's'}
    player_mapping = {'X': 'r', 'Y': 'p', 'Z': 's'}
    parsed_lines = []
    for l in lines:    
        parts = l.split()
        parsed = [opponent_mapping[parts[0]], player_mapping[parts[1]]]
        parsed_lines.append(parsed)
    return parsed_lines

def parse_input2(lines):
    opponent_mapping = {'A': 'r', 'B': 'p', 'C': 's'}
    outcome_mapping = {'X': 'l', 'Y': 'd', 'Z': 'w'}
    parsed_lines = []
    for l in lines:    
        parts = l.split()
        parsed = [opponent_mapping[parts[0]], outcome_mapping[parts[1]]]
        parsed_lines.append(parsed)
    return parsed_lines
    

def round_outcome(round):
    [opponent, player] = round
    if opponent == player:
        return 'd'
    
    if opponent == 'r' and player == 'p':
        return 'w'
    if opponent == 'p' and player == 's':
        return 'w'
    if opponent == 's' and player == 'r':
        return 'w'

    return 'l'
    

def score(round):
    outcome = round_outcome(round)
    shape_score = {'r': 1, 'p': 2, 's': 3}
    outcome_score = {'w': 6, 'l': 0, 'd': 3}
    return shape_score[round[1]] + outcome_score[outcome]

def round_shape(round):
    [opponent, outcome] = round
    if outcome == 'd':
        return opponent

    if opponent == 'r':
        return 'p' if outcome == 'w' else 's'
    if opponent == 'p':
        return 's' if outcome == 'w' else 'r'
    if opponent == 's':
        return 'r' if outcome == 'w' else 'p'
        
    

def score2(round):
    shape = round_shape(round)
    shape_score = {'r': 1, 'p': 2, 's': 3}
    outcome_score = {'w': 6, 'l': 0, 'd': 3}
    return shape_score[shape] + outcome_score[round[1]]


if __name__ == "__main__":
    lines = input_lines('day2_input.txt')

    parsed1 = parse_input1(lines)
    total_score1 = 0
    for round in parsed1:
        total_score1 += score(round)
    
    assert total_score1 == 14531

    parsed2 = parse_input2(lines)
    total_score2 = 0
    for round in parsed2:
        total_score2 += score2(round)
    
    assert total_score2 == 11258