# code for part 2

class Objects:
    def __init__(self, name, defeats, points, defpoints, winpoints):
        self.name = name
        self.defeats = defeats
        self.points = points
        self.defpoints = defpoints
        self.winpoints = winpoints

def choice(input):
    if input == "X" or input == "A":
        choice = Objects("Rock", "Scissors", 1, 3, 2)
    if input == "Y" or input == "B":
        choice = Objects("Paper", "Rock", 2, 1, 3)
    if input == "Z" or input == "C":
        choice = Objects("Scissors", "Paper", 3, 2, 1)
    return choice

def points(outcome, opchoice):
    points = 0
    op = choice(opchoice)
    if outcome == "X":
        points = 0 + op.defpoints
    if outcome == "Y":
        points = 3 + op.points
    if outcome == "Z":
        points = 6 + op.winpoints
    return points

f = open("day2_input.txt", "r")
highscore = 0
for line in f:
    choices = line.strip().split(" ")
    highscore += points(choices[1], choices[0])
f.close()
print(highscore)