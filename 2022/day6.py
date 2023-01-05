
def main():
    with open("/home/michael/tmp/input_d6.txt", "r") as input:
        for i in input:
            com = i.strip()
    print(part1(com))
    print(part2(com))

def part1(com):
    for n in range(len(com)):
        tmplist = []
        if n >= len(com) - 3:
            break
        for m in range(4):
            tmplist.append(com[n+m])
        lset = set(tmplist)

        if len(lset) == 4:
            print(f"set: {lset}, n: {n}")
            return n + 4

def part2(com):
    for n in range(len(com)):
        tmplist = []
        if n >= len(com) - 13:
            break
        for m in range(14):
            tmplist.append(com[n+m])
        lset = set(tmplist)

        if len(lset) == 14:
            print(f"set: {lset}, n: {n}")
            return n + 14
        
main()
