#code for part 2

def puzzle(input):
    with open(input) as f:
        count = 0
        for line in f:
            a, b = line.strip().split(',')[0].split('-'), line.strip().split(',')[1].split('-')

            if int(b[0]) <= int(a[1]) and int(b[1]) >= int(a[0]):
                print("overlap:")
                print(a[0], a[1])
                print(b[0], b[1])
                count += 1
            else:
                print("no")
                print(a[0], a[1])
                print(b[0], b[1])
        return count

print(puzzle('day4_input.txt'))