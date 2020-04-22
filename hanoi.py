import time

def output(towers):
    print()
    print("A",towers[0])
    print("B",towers[1])
    print("C",towers[2])
    print()

def move(f,t,towers):
    if f == 'A':
        disc = towers[0][-1]
        towers[0] = towers[0][:-1]
    elif f == 'B':
        disc = towers[1][-1]
        towers[1] = towers[1][:-1]
    else:
        disc = towers[2][-1]
        towers[2] = towers[2][:-1]
    if t == 'A':
        towers[0].append(disc)
    elif t == 'B':
        towers[1].append(disc)
    else:
        towers[2].append(disc)
    #print("Move disc from {} to {}".format(f,t))
    #output(towers)
    global moves
    moves += 1

def hanoi(n,f,h,t,tower):
    if n != 0:
        hanoi(n-1,f,t,h,tower)
        move(f,t,towers)
        hanoi(n-1,h,f,t,towers)

num = 20
for num in range(0,101):
    print()
    towers = [[],[],[]]
    for x in range(1,num+1):
        towers[0].append(x)
    moves = 0
    #output(towers)
    start = time.time()
    hanoi(num,'A','B','C',towers)
    end = time.time()
    print("For",num,"discs")
    print("Made", moves, "moves")
    print("Took",end-start,"seconds")