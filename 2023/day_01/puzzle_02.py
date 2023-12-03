import re

numbers = {
    "one":   1,
    "two":   2,
    "three": 3,
    "four":  4,
    "five":  5,
    "six":   6,
    "seven": 7,
    "eight": 8,
    "nine":  9
       }

def finder(line):
    res_dict = {}
    for n in (list(numbers.keys())+list(numbers.values())):
        for x in re.finditer(str(n), line):
            if len(x.group(0)) > 1:
                res_dict[x.start()] = str(numbers[x.group(0)])
            else:
                res_dict[x.start()] = x.group(0)
    return dict(sorted(res_dict.items()))

with open ("input", "r") as input:
    sum_of_all = 0
    for line in input:
        re_dict= finder(line)
        sum_of_all += int(list(re_dict.values())[0] + list(re_dict.values())[-1])
    print(int(sum_of_all))

