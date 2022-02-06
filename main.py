file = open(r"pc_list.txt", "r")
imported_pcs = file.read().replace("\n", ", ").split(", ") #change text from readable to list
keys = ['1a', 1, '1b', -1, '2a', 17, '2b', -17, '3a', 69, '3b', -69, '4a', 277, '4b', -277] #used to create unique sums for list comprehension
pc_counter = 0

pcs = [[], [], [], [], [], [], [], [], []]
for i, pc in enumerate(imported_pcs):
    if pc in keys:
        if i % 4 == 3:
            pcs[pc_counter].append(keys[keys.index(pc) + 1])
            pc_counter += 1
        else:
            pcs[pc_counter].append(keys[keys.index(pc) + 1])
    else:
        print("Unsupported Format")
        break

pc_counter = 0
rotations = 0
i = 0

combinations = []
one_tempList = []
two_tempList = []

x = 0
answer = []

def trial_error(x):
    global rotations, combinations, two_tempList, i, pc_counter, keys
    if x == 0:
        for p in pcs:
            while rotations < 4:
                p.insert(4, p.pop(0))
                t = p.copy()
                combinations.append([t])
                two_tempList.append([t])
                rotations += 1
            rotations = 0
        trial_error(x + 1)
    elif x == 1:
        one = combinations
        two = combinations
        for o in one:
            while i < len(two):
                if sum(two[i][0]) in [sum(y) for y in o]:
                    i += 1
                    pass
                else:
                    if o[0][2] + two[i][0][0] == 0:
                        one_tempList.extend([[o[0], two[i][0]]])
                        i += 1
                    else:
                        i += 1
                        pass
            i = 0
        trial_error(x + 1)
    elif x == 2:
        combinations.clear()
        one = one_tempList
        two = two_tempList
        for o in one:
            while i < len(two):
                if sum(two[i][0]) in [sum(y) for y in o]:
                    i += 1
                    pass
                else:
                    if o[1][3] + two[i][0][1] == 0:
                        combinations.extend([[o[0], o[1], two[i][0]]])
                        i += 1
                    else:
                        i += 1
                        pass
            i = 0
        trial_error(x + 1)
    elif x == 3:
        one_tempList.clear()
        one = combinations
        two = two_tempList
        for o in one:
            while i < len(two):
                if sum(two[i][0]) in [sum(y) for y in o]:
                    i += 1
                    pass
                else:
                    if o[2][0] + two[i][0][2] == 0 and o[0][3] + two[i][0][1] == 0:
                        one_tempList.extend([[o[0], o[1], o[2], two[i][0]]])
                        i += 1
                    else:
                        i += 1
                        pass
            i = 0
        trial_error(x + 1)
    elif x == 4:
        combinations.clear()
        one = one_tempList
        two = two_tempList
        for o in one:
            while i < len(two):
                if sum(two[i][0]) in [sum(y) for y in o]:
                    i += 1
                    pass
                else:
                    if o[3][3] + two[i][0][1] == 0:
                        combinations.extend([[o[0], o[1], o[2], o[3], two[i][0]]])
                        i += 1
                    else:
                        i += 1
                        pass
            i = 0
        trial_error(x + 1)
    elif x == 5:
        one_tempList.clear()
        one = combinations
        two = two_tempList
        for o in one:
            while i < len(two):
                if sum(two[i][0]) in [sum(y) for y in o]:
                    i += 1
                    pass
                else:
                    if o[4][2] + two[i][0][0] == 0 and o[2][3] + two[i][0][1] == 0:
                        one_tempList.extend([[o[0], o[1], o[2], o[3], o[4], two[i][0]]])
                        i += 1
                    else:
                        i += 1
                        pass
            i = 0
        trial_error(x + 1)
    elif x == 6:
        combinations.clear()
        one = one_tempList
        two = two_tempList
        for o in one:
            while i < len(two):
                if sum(two[i][0]) in [sum(y) for y in o]:
                    i += 1
                    pass
                else:
                    if o[5][2] + two[i][0][0] == 0:
                        combinations.extend([[o[0], o[1], o[2], o[3], o[4], o[5], two[i][0]]])
                        i += 1
                    else:
                        i += 1
                        pass
            i = 0
        trial_error(x + 1)
    elif x == 7:
        one_tempList.clear()
        one = combinations
        two = two_tempList
        for o in one:
            while i < len(two):
                if sum(two[i][0]) in [sum(y) for y in o]:
                    i += 1
                    pass
                else:
                    if o[6][1] + two[i][0][3] == 0 and o[2][2] + two[i][0][0] == 0:
                        one_tempList.extend([[o[0], o[1], o[2], o[3], o[4], o[5], o[6], two[i][0]]])
                        i += 1
                    else:
                        i += 1
                        pass
            i = 0
        trial_error(x + 1)
    elif x == 8:
        combinations.clear()
        one = one_tempList
        two = two_tempList
        for o in one:
            while i < len(two):
                if sum(two[i][0]) in [sum(y) for y in o]:
                    i += 1
                    pass
                else:
                    if o[7][1] + two[i][0][3] == 0 and o[1][2] + two[i][0][0] == 0:
                        combinations.extend([[o[0], o[1], o[2], o[3], o[4], o[5], o[6], o[7], two[i][0]]])
                        i += 1
                    else:
                        i += 1
                        pass
            i = 0
        for a, combo in enumerate(combinations):
            for b, com in enumerate(combo):
                for e, c in enumerate(com):
                    if c in keys:
                        combinations[a][b][e] = keys[keys.index(c) - 1]
                    else:
                        print("Unsupported Format")
                        break
            print(combo)


trial_error(x)
