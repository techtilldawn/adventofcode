with open ("input", "r") as input:
    all_sum = 0
    for line in input:
        tmp = line.split(":")
        game = tmp[0]
        sets = tmp[1].split(";")
        cube_dic = {"blue": 0, "green": 0, "red": 0}
        for set in sets:
            cubes = set.split(",")
            for cube in cubes:
                cm = cube.strip().split(" ")
                if int(cm[0]) > cube_dic[cm[1]]:
                   cube_dic[cm[1]] = int(cm[0]) 
        values = list(cube_dic.values())
        res = 1
        for x in values:
            res = res * x
        all_sum += res
    print(all_sum)