'''Counting score of rock, paper, scissor game from secret strategy guides'''
with open('day2_input.txt', encoding='utf-8') as f:
    strategy_guide = [line.rstrip() for line in f.readlines()]
score = []
score_secret_strategy = []
WIN = 6
DRAW = 3
LOST = 0
ROCK = 1
PAPER = 2
SCISSORS = 3

for game in strategy_guide:
    if game == 'A X':
        score.append(ROCK+DRAW)
    elif game == 'A Y':
        score.append(PAPER+WIN)
    elif game == 'A Z':
        score.append(SCISSORS+LOST)
    elif game == 'B X':
        score.append(ROCK+LOST)
    elif game == 'B Y':
        score.append(PAPER+DRAW)
    elif game == 'B Z':
        score.append(SCISSORS+WIN)
    elif game == 'C X':
        score.append(ROCK+WIN)
    elif game == 'C Y':
        score.append(PAPER+LOST)
    elif game == 'C Z':
        score.append(SCISSORS+DRAW)

for game in strategy_guide:
    if game == 'A X':
        score_secret_strategy.append(SCISSORS+LOST)
    elif game == 'A Y':
        score_secret_strategy.append(ROCK+DRAW)
    elif game == 'A Z':
        score_secret_strategy.append(PAPER+WIN)
    elif game == 'B X':
        score_secret_strategy.append(ROCK+LOST)
    elif game == 'B Y':
        score_secret_strategy.append(PAPER+DRAW)
    elif game == 'B Z':
        score_secret_strategy.append(SCISSORS+WIN)
    elif game == 'C X':
        score_secret_strategy.append(PAPER+LOST)
    elif game == 'C Y':
        score_secret_strategy.append(SCISSORS+DRAW)
    elif game == 'C Z':
        score_secret_strategy.append(ROCK+WIN)

print(sum(score_secret_strategy))