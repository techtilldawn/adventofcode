with open ("input", "r") as input:
    game_rules = {"red": 12, "green": 13, "blue": 14}
    id_sum = 0
    for line in input:
        game_possible = True
        tmp = line.split(":")
        game = tmp[0]
        sets = tmp[1].split(";")
        for set in sets:
            cubes = set.split(",")
            for cube in cubes:
                cm = cube.strip().split(" ")
                if int(cm[0]) > game_rules[cm[1]]:
                    game_possible = False
        if game_possible:
            id_sum += int(game.split(" ")[1])
        print(id_sum)