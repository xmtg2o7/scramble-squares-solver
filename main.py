#Assigned each variable a numerical value
vik = 1
ing = -1
hel = 2
met = -2
jer = 3
sey = -3
horns = 7
face = -7

#Created the pieces - I used the sums later to know when I was comparing a piece to an already used piece.
piece_1 = [sey, jer, face, vik]    #Sum -6
piece_2 = [hel, vik, face, sey]    #Sum -7
piece_3 = [horns, vik, met, hel]   #Sum 8
piece_4 = [ing, sey, hel, horns]   #Sum 5
piece_5 = [hel, face, sey, ing]    #Sum -9
piece_6 = [jer, hel, vik, face]    #Sum -1
piece_7 = [sey, vik, horns, met]   #Sum 3
piece_8 = [horns, vik, jer, hel]   #Sum 13
piece_9 = [met, ing, horns, sey]   #Sum 1

#List of all pieces
pieces = [piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7, piece_8, piece_9]

#In other attempts I needed a second varsion of pieces, so this 'pcs' variable is redundent, but also the one I used.
pcs = pieces

#Used later to keep track of the number of times a piece was rotated
rotations = 0

#Used for iteration
i = 0

#Empty lists to append to
#combinations ends up being every piece with every form of rotation
combinations = []
#both tempLists are used for succesfull combinations. I alternate between the two below.
one_tempList = []
two_tempList = []

#I played with recursion in an earlier attempt; however, using a function for each stage was easier for me to work with and debug
def stage_one():
    global rotations, combinations, two_tempList
    #iterate through pcs and create a list of every position
    for p in pcs:
        while rotations < 4:
            p.insert(4, p.pop(0))
            t = p.copy()
            combinations.append([t])
            two_tempList.append([t])
            rotations += 1
        rotations = 0
    stage_two()

def stage_two():
    global i, combinations, two_tempList
    one = combinations
    two = combinations
    #I alternate between the temp lists. In this first instance, I'm just looking for any combination that matches the original list of pieces and adding it to list one
    for o in one:
        while i < len(two):
            #Since the sums are unique, I used this to check if the piece is comparing it to itself. In earlier versions, I tried comparing the list and sort order but it was very cumbersome.
            if sum(o[0]) == sum(two[i][0]):
                i += 1
                pass
            else:
                #if the pieces are not the same and side 2 (right side) matches side 0 (left side), it addes it to list one in a nested list
                if o[0][2] + two[i][0][0] == 0:
                    one_tempList.extend([[o[0], two[i][0]]])
                    i += 1
                else:
                    i += 1
                    pass
        i = 0
    stage_three()

def stage_three():
    global i, combinations, one_tempList, two_tempList
    combinations.clear()
    one = one_tempList
    two = two_tempList
    for o in one:
        while i < len(two):
            #these essentially repeat, just with logic added to compare the each piece as they get added.
            if sum(o[0]) == sum(two[i][0]) \
                    or sum(o[1]) == sum(two[i][0]):
                i += 1
                pass
            else:
                #I lied earlier, I alternate between combintions and one_tempList...
                if o[1][3] + two[i][0][1] == 0:
                    combinations.extend([[o[0], o[1], two[i][0]]])
                    i += 1
                else:
                    i += 1
                    pass
        i = 0
    stage_four()

#I had something wrong with my code originally and was hitting almost 400,000 combinations by this point when going across the top row for comparissons.
# I changed the route to go upper left, upper middle, middle middle, middle left so that I piece 4 was comparing two side instead of one.
# This brought it down to 50,000 combinations which still took forever to load by the fifth stage. Long story short, I found an error in my logic and, upon fixing, ended up with 212 results.

#Original route:
#  1→   2→   3↓
# ↓6↑  ←5↑  ←4
#  7→  ↑8→  ↑9

#Final route:
#  1→   2↓  ←9
# ↑4↓  ←3   ←8↑
#  5→  ↑6→   7↑

def stage_four():
    global i, combinations, one_tempList
    one_tempList.clear()
    one = combinations
    two = two_tempList
    for o in one:
        while i < len(two):
            if sum(o[0]) == sum(two[i][0]) \
                    or sum(o[1]) == sum(two[i][0]) \
                    or sum(o[2]) == sum(two[i][0]):
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
    stage_five()

def stage_five():
    global i, combinations, one_tempList
    combinations.clear()
    one = one_tempList
    two = two_tempList
    for o in one:
        while i < len(two):
            if sum(o[0]) == sum(two[i][0]) \
                    or sum(o[1]) == sum(two[i][0]) \
                    or sum(o[2]) == sum(two[i][0]) \
                    or sum(o[3]) == sum(two[i][0]):
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
    stage_six()

def stage_six():
    global i, combinations, one_tempList
    one_tempList.clear()
    one = combinations
    two = two_tempList
    for o in one:
        while i < len(two):
            if sum(o[0]) == sum(two[i][0]) \
                    or sum(o[1]) == sum(two[i][0]) \
                    or sum(o[2]) == sum(two[i][0]) \
                    or sum(o[3]) == sum(two[i][0]) \
                    or sum(o[4]) == sum(two[i][0]):
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
    stage_seven()

def stage_seven():
    global i, combinations, one_tempList
    combinations.clear()
    one = one_tempList
    two = two_tempList
    for o in one:
        while i < len(two):
            if sum(o[0]) == sum(two[i][0]) \
                    or sum(o[1]) == sum(two[i][0]) \
                    or sum(o[2]) == sum(two[i][0]) \
                    or sum(o[3]) == sum(two[i][0]) \
                    or sum(o[4]) == sum(two[i][0]) \
                    or sum(o[5]) == sum(two[i][0]):
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
    stage_eight()

def stage_eight():
    global i, combinations, one_tempList
    one_tempList.clear()
    one = combinations
    two = two_tempList
    for o in one:
        while i < len(two):
            if sum(o[0]) == sum(two[i][0]) \
                    or sum(o[1]) == sum(two[i][0]) \
                    or sum(o[2]) == sum(two[i][0]) \
                    or sum(o[3]) == sum(two[i][0]) \
                    or sum(o[4]) == sum(two[i][0]) \
                    or sum(o[5]) == sum(two[i][0]) \
                    or sum(o[6]) == sum(two[i][0]):
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
    stage_nine()

def stage_nine():
    global i, combinations, one_tempList
    combinations.clear()
    one = one_tempList
    two = two_tempList
    for o in one:
        while i < len(two):
            if sum(o[0]) == sum(two[i][0]) \
                    or sum(o[1]) == sum(two[i][0]) \
                    or sum(o[2]) == sum(two[i][0]) \
                    or sum(o[3]) == sum(two[i][0]) \
                    or sum(o[4]) == sum(two[i][0]) \
                    or sum(o[5]) == sum(two[i][0]) \
                    or sum(o[6]) == sum(two[i][0]) \
                    or sum(o[7]) == sum(two[i][0]):
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
    #updated my code and now have 4 succesfull combinations. I've only tried the one I took a screenshot of, but the rest appear legit.
    #Oddly enough, I would have expected the results to have a forward version and a backward version, but I'm not seeing it. Not sure why.
    for combo in combinations:
        #only annoying part is that the pieces are listed as their numerical value, so one must compare them to their original lists to see which piece is which
        # and what orientation it needs to be in. I thought about making a web app to visualize all solutions, as this should work for any puzzle variant, but I'm
        #probably not going to do that...
        print(f'Successful combo using: {combo}')

stage_one()


#Second attempt - used recursion here and tried to go piece by piece. It's built on logical errors so there wasn't much for saving it.
def p_solver(p):
    global rotations, solved, pieces, pcs
    if solved == 1:
        print('Success')
        print(puzzle)
    else:
        print(len(puzzle), p, len(pcs))
        if rotations == 4:
            pcs.clear()
            puzzle.clear()
            tried_pcs.clear()
            pcs.extend(pieces)
            random.shuffle(pcs)
            rotations = 0
            p_solver(8)
        elif len(puzzle) == 0:
            puzzle.append(pcs[p])
            pcs.pop(p)
            p_solver(p-1)
        elif p < 0:
            puzzle.pop(len(puzzle)-1)
            tried_pcs.pop(len(tried_pcs)-1)
            pcs.clear()
            pcs.extend(tried_pcs)
            p_solver(p-1)
        elif len(puzzle) < 3:
            if puzzle[len(puzzle)-1][2] + pcs[p][0] == 0:
                puzzle.append(pcs[p])
                pcs.pop(p)
                tried_pcs.append(pcs[p])
                p_solver(len(pcs) - 1)
            elif puzzle[len(puzzle)-1][2] + pcs[p][1] == 0:
                pc_zero = pcs[p].pop(0)
                pcs[p].insert(4, pc_zero)
                puzzle.append(pcs[p])
                pcs.pop(p)
                tried_pcs.append(pcs[p])
                p_solver(len(pcs) - 1)
            elif puzzle[len(puzzle)-1][2] + pcs[p][2] == 0:
                pc_zero = pcs[p].pop(0)
                pc_one = pcs[p].pop(0)
                pcs[p].extend([pc_zero, pc_one])
                puzzle.append(pcs[p])
                pcs.pop(p)
                tried_pcs.append(pcs[p])
                p_solver(len(pcs) - 1)
            elif puzzle[len(puzzle)-1][2] + pcs[p][3] == 0:
                pc_three = pcs[p].pop(3)
                pcs[p].insert(0, pc_three)
                puzzle.append(pcs[p])
                pcs.pop(p)
                tried_pcs.append(pcs[p])
                p_solver(len(pcs) - 1)
            else:
                p_solver(p-1)
        elif len(puzzle) == 3 or len(puzzle) == 6:
            if puzzle[2][3] + pcs[p][1] == 0:
                puzzle.append(pcs[p])
                pcs.pop(p)
                tried_pcs.append(pcs[p])
                p_solver(len(pcs) - 1)
            elif puzzle[2][3] + pcs[p][2] == 0:
                pc_zero = pcs[p].pop(0)
                pcs[p].insert(4, pc_zero)
                puzzle.append(pcs[p])
                pcs.pop(p)
                tried_pcs.append(pcs[p])
                p_solver(len(pcs) - 1)
            elif puzzle[2][3] + pcs[p][3] == 0:
                pc_zero = pcs[p].pop(0)
                pc_one = pcs[p].pop(0)
                pcs[p].extend([pc_zero, pc_one])
                puzzle.append(pcs[p])
                tried_pcs.append(pcs[p])
                p_solver(p - 1)
            elif puzzle[2][3] + pcs[p][0] == 0:
                pc_three = pcs[p].pop(3)
                pcs[p].insert(0, pc_three)
                puzzle.append(pcs[p])
                pcs.pop(p)
                tried_pcs.append(pcs[p])
                p_solver(len(pcs) - 1)
            else:
                p_solver(p - 1)
        elif len(puzzle) == 4:
            if puzzle[3][0] + pcs[p][2] == 0 and puzzle[1][3] + pcs[p][1] == 0:
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(3)
            elif puzzle[3][0] + pcs[p][3] == 0 and puzzle[1][3] + pcs[p][2] == 0:
                pc_zero = pcs[p].pop(0)
                pcs[p].insert(4, pc_zero)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(3)
            elif puzzle[3][0] + pcs[p][0] == 0 and puzzle[1][3] + pcs[p][3] == 0:
                pc_zero = pcs[p].pop(0)
                pc_one = pcs[p].pop(0)
                pcs[p].extend([pc_zero, pc_one])
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(3)
            elif puzzle[3][0] + pcs[p][1] == 0 and puzzle[1][3] + pcs[p][0] == 0:
                pc_three = pcs[p].pop(3)
                pcs[p].insert(0, pc_three)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(3)
            else:
                p_solver(p - 1)
        elif len(puzzle) == 5:
            if puzzle[4][0] + pcs[p][2] == 0 and puzzle[0][3] + pcs[p][1] == 0:
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(4)
            elif puzzle[4][0] + pcs[p][3] == 0 and puzzle[0][3] + pcs[p][2] == 0:
                pc_zero = pcs[p].pop(0)
                pcs[p].insert(4, pc_zero)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(4)
            elif puzzle[4][0] + pcs[p][0] == 0 and puzzle[0][3] + pcs[p][3] == 0:
                pc_zero = pcs[p].pop(0)
                pc_one = pcs[p].pop(0)
                pcs[p].extend([pc_zero, pc_one])
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(4)
            elif puzzle[4][0] + pcs[p][1] == 0 and puzzle[0][3] + pcs[p][0] == 0:
                pc_three = pcs[p].pop(3)
                pcs[p].insert(0, pc_three)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(4)
            else:
                p_solver(p - 1)
        elif len(puzzle) == 7:
            if puzzle[6][2] + pcs[p][0] == 0 and puzzle[4][3] + pcs[p][1] == 0:
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(6)
            elif puzzle[6][2] + pcs[p][1] == 0 and puzzle[4][3] + pcs[p][2] == 0:
                pc_zero = pcs[p].pop(0)
                pcs[p].insert(4, pc_zero)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(6)
            elif puzzle[6][2] + pcs[p][2] == 0 and puzzle[4][3] + pcs[p][3] == 0:
                pc_zero = pcs[p].pop(0)
                pc_one = pcs[p].pop(0)
                pcs[p].extend([pc_zero, pc_one])
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(6)
            elif puzzle[6][2] + pcs[p][3] == 0 and puzzle[4][3] + pcs[p][0] == 0:
                pc_three = pcs[p].pop(3)
                pcs[p].insert(0, pc_three)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(6)
            else:
                p_solver(p - 1)
        elif len(puzzle) == 8:
            if puzzle[7][2] + pcs[p][0] == 0 and puzzle[3][3] + pcs[p][1] == 0:
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(7)
            elif puzzle[7][2] + pcs[p][1] == 0 and puzzle[3][3] + pcs[p][2] == 0:
                pc_zero = pcs[p].pop(0)
                pcs[p].insert(4, pc_zero)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(7)
            elif puzzle[7][2] + pcs[p][2] == 0 and puzzle[3][3] + pcs[p][3] == 0:
                pc_zero = pcs[p].pop(0)
                pc_one = pcs[p].pop(0)
                pcs[p].extend([pc_zero, pc_one])
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(7)
            elif puzzle[7][2] + pcs[p][3] == 0 and puzzle[3][3] + pcs[p][0] == 0:
                pc_three = pcs[p].pop(3)
                pcs[p].insert(0, pc_three)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(7)
            else:
                p_solver(p - 1)
        else:
            print('this should not be here')


#First real attempt. Also built on logical errors. I thought I had them figured out when I moved on to the second attempt.
def p_solver(p):
    global rotations, solved
    pieces = [piece_1, piece_2, piece_3, piece_4, piece_5, piece_6, piece_7, piece_8, piece_9]
    if solved == 1:
        print('Success')
        print(puzzle)
    else:
        print(len(puzzle), p, len(pcs))
        if rotations == 4:
            pcs.clear()
            puzzle.clear()
            tried_pcs.clear()
            pcs.extend(pieces)
            random.shuffle(pcs)
            rotations = 0
            p_solver(8)
        elif len(puzzle) == 9:
            if puzzle[3][3] + puzzle[8][1] == 0 and puzzle[4][3] + puzzle[7][1] == 0 and puzzle[1][3] + puzzle[4][1] == 0 and puzzle[0][3] + puzzle[5][1] == 0:
                solved = 1
                p_solver(p)
            else:
                pcs.clear()
                tried_pcs.clear()
                pcs.extend(pieces)
                puzzle.clear()
                if rotations == 0:
                    print('clockwise2')
                    pc_three = pcs[8].pop(3)
                    pcs[8].insert(0, pc_three)
                elif rotations == 1:
                    print('1802')
                    pc_zero = pcs[8].pop(0)
                    pc_one = pcs[8].pop(0)
                    pcs[8].extend([pc_zero, pc_one])
                else:
                    print('counter2')
                    pc_zero = pcs[8].pop(0)
                    pcs[8].insert(4, pc_zero)
                print(pcs[8])
                rotations += 1
                p_solver(8)
        elif p < 0 and len(pcs) > 1 and pcs[0] not in tried_pcs:
            pcs.insert(0, puzzle[len(puzzle) - 1])
            tried_pcs.append(puzzle[len(puzzle)-1])
            puzzle.pop(len(puzzle) - 1)
            p_solver(len(pcs) - 1)
        elif p < 0 and len(pcs) == 1 or pcs[0] in tried_pcs:
            pcs.clear()
            tried_pcs.clear()
            pcs.extend(pieces)
            puzzle.clear()
            if rotations == 0:
                print('clockwise')
                pc_three = pcs[8].pop(3)
                pcs[8].insert(0, pc_three)
            elif rotations == 1:
                print('180')
                pc_zero = pcs[8].pop(0)
                pc_one = pcs[8].pop(0)
                pcs[8].extend([pc_zero, pc_one])
            else:
                print('counter')
                pc_zero = pcs[8].pop(0)
                pcs[8].insert(4, pc_zero)
            print(pcs[8])
            rotations += 1
            p_solver(8)
        elif len(puzzle) == 0:
            puzzle.append(pcs[p])
            pcs.pop(p)
            p_solver(p-1)
        elif len(puzzle) < 3 or 6 < len(puzzle) < 9:
            if puzzle[len(puzzle)-1][2] + pcs[p][0] == 0:
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(len(pcs) - 1)
            elif puzzle[len(puzzle)-1][2] + pcs[p][1] == 0:
                pc_zero = pcs[p].pop(0)
                pcs[p].insert(4, pc_zero)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(len(pcs) - 1)
            elif puzzle[len(puzzle)-1][2] + pcs[p][2] == 0:
                pc_zero = pcs[p].pop(0)
                pc_one = pcs[p].pop(0)
                pcs[p].extend([pc_zero, pc_one])
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(len(pcs) - 1)
            elif puzzle[len(puzzle)-1][2] + pcs[p][3] == 0:
                pc_three = pcs[p].pop(3)
                pcs[p].insert(0, pc_three)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(len(pcs) - 1)
            else:
                p_solver(p-1)
        elif len(puzzle) == 3 or len(puzzle) == 6:
            if puzzle[len(puzzle)-1][3] + pcs[p][1] == 0:
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(len(pcs) - 1)
            elif puzzle[len(puzzle)-1][3] + pcs[p][2] == 0:
                pc_zero = pcs[p].pop(0)
                pcs[p].insert(4, pc_zero)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(len(pcs) - 1)
            elif puzzle[len(puzzle)-1][3] + pcs[p][3] == 0:
                pc_zero = pcs[p].pop(0)
                pc_one = pcs[p].pop(0)
                pcs[p].extend([pc_zero, pc_one])
                puzzle.append(pcs[p])
                p_solver(p - 1)
            elif puzzle[len(puzzle)-1][3] + pcs[p][0] == 0:
                pc_three = pcs[p].pop(3)
                pcs[p].insert(0, pc_three)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(len(pcs) - 1)
            else:
                p_solver(p - 1)
        elif 3 < len(puzzle) < 6:
            if puzzle[len(puzzle) - 1][0] + pcs[p][2] == 0:
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(len(pcs) - 1)
            elif puzzle[len(puzzle) - 1][0] + pcs[p][3] == 0:
                pc_zero = pcs[p].pop(0)
                pcs[p].insert(4, pc_zero)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(len(pcs) - 1)
            elif puzzle[len(puzzle) - 1][0] + pcs[p][0] == 0:
                pc_zero = pcs[p].pop(0)
                pc_one = pcs[p].pop(0)
                pcs[p].extend([pc_zero, pc_one])
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(len(pcs) - 1)
            elif puzzle[len(puzzle) - 1][0] + pcs[p][1] == 0:
                pc_three = pcs[p].pop(3)
                pcs[p].insert(0, pc_three)
                puzzle.append(pcs[p])
                pcs.pop(p)
                p_solver(len(pcs) - 1)
            else:
                p_solver(p - 1)
        else:
            print('this should not be here')
