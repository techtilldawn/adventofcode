import re

with open ("input", "r") as input:
    sum_of_all = 0
    for line in input:
        out = re.findall(r"\d", line)
        sum_of_all += int(out[0] + out[-1])
    print(int(sum_of_all))