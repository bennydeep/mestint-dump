
"""ha lett volna megfelelő idő és megfelelő tudás, akkor ebből lett volna a saját megoldás"""

import numpy as np
import random

gameid="8x8:bwbwbwbwwbwbwbwbbwbwbwbwwbwbwbwbbwbwbwbwwbwbwbwbbwbwbwbwwbwbwbwb"
a=gameid.split(":")
b=list(a[1])
n=int((gameid.split(":")[0].split("x"))[0])
m=int((gameid.split(":")[0].split("x"))[1])
grid=(np.reshape(b,(n,m)))
#grid=(np.reshape(b,(8,8)))

#print(grid)
print(np.matrix(grid))
#print(grid[1][1])
print()


def elsolevett(matrix):
    # n = int((gameid.split(":")[0].split("x"))[0])
    # m = int((gameid.split(":")[0].split("x"))[1])
    for x in range(n):
        for y in range(m):
            if matrix[x][y]==" ":
                return (x, y)
turn=1
while turn==1:
    print("a fekete kezd, a fehér random játékos")
    a="b"
    if a == "b":
        print("a b lépés lehetőségei: 1,1 4,4 5,5 8,8")
        b=int(input("melyiket veszed le ? "))
        if b==11:
            grid[0][0]=' '
        if b==44:
            grid[3][3]=' '
        if b==55:
            grid[4][4]=' '
        if b==88:
            grid[7][7]=' '
        print(grid)
        print(" a w lép")
        choiceList = []
        x = elsolevett(grid)[0]
        y = elsolevett(grid)[1]
        if grid [0][0]==" ":
            choiceList.append([0, 1])
            choiceList.append([1, 0])
        elif grid[7][7] == ".":
            choiceList.append([7,6])
            choiceList.append([6,7]*2)
        else:

            choiceList.append([x, y- 1])
            choiceList.append([x+ 1, y] )
            choiceList.append([x, y+ 1] )
            choiceList.append([x - 1, y])

        print(choiceList)

        c= (random.choice(choiceList))
        print(c[1])
        grid[c[0],c[1]]=" "
        print(grid)
        turn+=1
        while turn==2:
            print(grid)