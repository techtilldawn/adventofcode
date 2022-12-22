#code for part 2

import string
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)

def get_points (letter):
    print("current: ", letter)
    if letter in lower:
        for i in range(len(lower)):
            if letter == lower[i]:
                print(str(i+1), x)
                return int(i + 1)
    if letter in upper:
        for i in range(len(upper)):
            if letter == upper[i]:
                print(str(i+27), x)
                return int(i + 27)

with open('day3_input.txt') as f:
    prio = 0
    count = 0
    compare = []
    for line in f:
        compare.append(line.strip())
        count += 1
        if count == 3:
            done = False
            for x in compare[0]:
                if x in compare[1] and x in compare[2] and done != True:
                    prio += get_points(x)
                    done = True
            count = 0
            compare = []

print(prio)

