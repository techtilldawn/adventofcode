def main():
    with open ("/home/michael/tmp/input_d5.txt", "r") as input:
        obj = {}
        firsttime = True
        for i in range(1, 10):
            obj[str(i)] = []
        for row in input:
            if "[" in row:
                tmprow = row.strip()
                count = 0
                for n in range(1, len(row), 4):
                    count += 1
                    if tmprow[n].isalpha():
                        obj[str(count)].append(tmprow[n])
            
            if "move" in row:
                if firsttime:
                    for i in obj:
                        obj[i].reverse()
                    firsttime = False
                cmdlist = row.strip().split(" ")
                obj = crate_mover_9001(obj, cmdlist[3], cmdlist[5], int(cmdlist[1]))
                
    for i in range(1, len(obj)+1):
        print(obj[str(i)][-1], end="")
    print()


def crate_mover_9000(obj, f, t, amt):
    for i in range(amt): 
        obj[t].append(obj[f][-1])
        obj[f].pop()
    return obj

def crate_mover_9001(obj, f, t, amt):
    for i in range(-amt, 0, 1): 
        obj[t].append(obj[f][i])
        obj[f].pop(i)
    return obj

main()
