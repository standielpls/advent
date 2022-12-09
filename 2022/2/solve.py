f = open('input.txt', 'r')

key_legend = {
    'A': "rock", # rock
    'B': "paper", # paper
    'C': "scissor", # scissor
}

wins = {
    'rock': 'scissor',
    'scissor': 'paper',
    'paper': 'rock',
}

losses = {
    'rock': 'paper',
    'paper': 'scissor',
    'scissor': 'rock',
}

item_score = {
    "rock": 1,
    "paper": 2,
    "scissor": 3,
}

puzzle_legend = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

# W = 6, D = 3, L = 0

def convert_to_item(key):
    return key_legend[key]

WIN_SCORE = 6
TIE_SCORE = 3
LOSS_SCORE = 0

def calculate(val1, val2):
    if val1 == val2:
        return TIE_SCORE
    
    if val1 == "rock" and val2 == "paper" or val1 == "paper" and val2 == "scissor" or val1 == "scissor" and val2 == "rock":
        return WIN_SCORE

    return LOSS_SCORE

def win_draw_lose(val):
    return puzzle_legend[val]
def part_one(f):
    count = 0 
    for line in f:
        if line.isspace():
            continue

        ss = line.rstrip().split(" ")
        opponent = convert_to_item(ss[0])
        # me = convert_to_item(ss[1])

        outcome = win_draw_lose(ss[1])
        me = None
        
        tool = None
        if outcome == "win":
            tool = losses
        elif outcome == "lose":
            tool = wins
        
        if tool is None:
            me = opponent
        else:
            me = tool[opponent]

        count += calculate(opponent, me)
        count += item_score[me]
    print(count)

part_one(f)