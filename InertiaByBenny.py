import numpy as np
import random

#8x8:mmsbgsmbgsbwsmbwwgmswbbmgmwgsswmbgmggsgsmbbwwgwsmbbSwbgwswbsbgmb
gameid="10x8:wwmwgbsmmmwbwsbggbgswsbmmwgmsgbsbwmwwwggmgbmsmsbgwsbswwbwmsmgsmgbsssggwgbbmSsgbm"
#gameid="10x8:wbwgmgmwbmwbssgssbggbwssbggmmsbwbmwswmbmmsbmgwwSgsmsgbssssmbmmgggwwwggbmwmgswbbw"
#gameid="10x8:wbsmmbSbgggmswsswswmssbmmswmgbwwgwbgbggsmmsbggsmmgbwgwwsbgwsmswmbsgwmbwmmbgbgwsb"
#gameid="10x8:wwsbmmswwbmgbgwsgssmgwsgbswmwgbmwmbggbwbmsgsmsmswsbgmsswgbwwmsbwgmmggwggbbsmbmSb"
#gameid="10x10:bbgswwsmggssswmwgSsgsgwsmbmbmgbbwbmmmwswwbbmwswgbggsgmbmgbgsmgmbgwgwwwbmsmsssgwbmgbbbgmmmsswwsgwsbwm"
#gameid="8x8:wwsswbwsbsmggsgbbmbbsbmsmbSmgsmgmgmwswmbswwmbgmbsbbbggbwwmgwggsw"
#gameid="10x8:bbgmbwwwmwmwbggSbmmwwsbmgwgsbbgmgmbsswbmgbmswsgsgsmsmmbwwwgmwsbswgbsbmsmssggggsw"
a=gameid.split(":")
b=list(a[1])
#print(b)
"""grid= [["m","m","s","b","g","s","m","b"],
        ["g","s","b","w","s","m","b","w"],
        ["w","g","m","s","w","b","b","m"],
        ["g","m","w","g","s","s","w","m"],
        ["b","g","m","g","g","s","g","s"],
        ["m","b","b","w","w","g","w","s"],
        ["m","b","b","S","w","b","g","w"],
        ["s","w","b","s","b","g","m","b"],]"""
m=int((gameid.split(":")[0].split("x"))[0])
n=int((gameid.split(":")[0].split("x"))[1])
grid=(np.reshape(b,(n,m)))
#grid=(np.reshape(b,(8,8)))

#print(grid)
print(np.matrix(grid))
#print(grid[1][1])
print()

def holalabda(matrix):
        #n = int((gameid.split(":")[0].split("x"))[0])
        #m = int((gameid.split(":")[0].split("x"))[1])
        for x in range(n):
                for y in range(m):
                        if matrix[x][y].isupper():
                                return (x, y)

#print (holalabda(grid))
def gemsnum(matrix):
        #n = int((gameid.split(":")[0].split("x"))[0])
        #m = int((gameid.split(":")[0].split("x"))[1])
        i=0
        for x in range(n):
                for y in range(m):
                        if matrix[x][y]=="g":
                                i+=1
        return i

def isitawin():
        if gemsnum(grid)==0:
                return True
        else:
                return False

def jobbra():
        x = holalabda(grid)[0]
        y = holalabda(grid)[1]
        grid[x][y]=grid[x][y].lower()
        grid[x][y+1]=grid[x][y+1].upper()
        pickupgem()

def balra():
        x = holalabda(grid)[0]
        y = holalabda(grid)[1]
        grid[x][y]=grid[x][y].lower()
        grid[x][y-1]=grid[x][y-1].upper()
        pickupgem()


def fel():
        x = holalabda(grid)[0]
        y = holalabda(grid)[1]
        grid[x][y]=grid[x][y].lower()
        grid[x-1][y]=grid[x-1][y].upper()
        pickupgem()

def le():
        x = holalabda(grid)[0]
        y = holalabda(grid)[1]
        grid[x][y]=grid[x][y].lower()
        grid[x+1][y]=grid[x+1][y].upper()
        pickupgem()

def jobbrafel():
        x = holalabda(grid)[0]
        y = holalabda(grid)[1]
        grid[x][y]=grid[x][y].lower()
        grid[x-1][y+1]=grid[x-1][y+1].upper()
        pickupgem()

def jobbrale():
        x = holalabda(grid)[0]
        y = holalabda(grid)[1]
        grid[x][y]=grid[x][y].lower()
        grid[x+1][y+1]=grid[x+1][y+1].upper()
        pickupgem()

def balrafel():
        x = holalabda(grid)[0]
        y = holalabda(grid)[1]
        grid[x][y]=grid[x][y].lower()
        grid[x-1][y-1]=grid[x-1][y-1].upper()
        pickupgem()

def balrale():
        x = holalabda(grid)[0]
        y = holalabda(grid)[1]
        grid[x][y]=grid[x][y].lower()
        grid[x+1][y-1]=grid[x+1][y-1].upper()
        pickupgem()

def ismine():
        c=False
        x = holalabda(grid)[0]
        y = holalabda(grid)[1]
        if grid[x][y]=="M":
                c=True
        return c

def isitsafe(move):
        if not ismine():
                return True
        else:
                return False

def pickupgem():
        x = holalabda(grid)[0]
        y = holalabda(grid)[1]
        if grid[x][y] == "G":
                grid[x][y]="B"

def slidebalra():
        while True:
                if not ismine():
                        try:
                                x = holalabda(grid)[0]
                                y = holalabda(grid)[1]
                                if grid[x][y - 1] == "w":
                                        break
                                if y==0:
                                        break
                                if grid[x][y - 1] == "s":
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x][y - 1] = grid[x][y - 1].upper()
                                        pickupgem()
                                        break
                                else:
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x][y - 1] = grid[x][y - 1].upper()
                                        pickupgem()
                        except IndexError:
                                break
                else:
                        break

def slidejobbra():
        while True:
                if not ismine():
                        try:
                                x = holalabda(grid)[0]
                                y = holalabda(grid)[1]
                                if grid[x][y+1]=="w":
                                        break
                                if y==m-1:
                                        break
                                if grid[x][y+1] == "s":
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x][y + 1] = grid[x][y + 1].upper()
                                        pickupgem()
                                        break
                                else:
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x][y + 1] = grid[x][y + 1].upper()
                                        pickupgem()
                        except IndexError:
                                break
                else:

                        break

def slidefel():
        while True:
                if not ismine():
                        try:
                                x = holalabda(grid)[0]
                                y = holalabda(grid)[1]
                                if grid[x-1][y]=="w":
                                        break
                                if x==0:
                                        break
                                if grid[x-1][y] == "s":
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x-1][y] = grid[x-1][y].upper()
                                        pickupgem()
                                        break
                                else:
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x-1][y] = grid[x-1][y].upper()
                                        pickupgem()
                        except IndexError:
                                break
                else:
                        break

def slidele():
        while True:
                if not ismine():
                        try:
                                x = holalabda(grid)[0]
                                y = holalabda(grid)[1]
                                if grid[x+1][y]=="w":
                                        break
                                if x==n-1:
                                        break
                                if grid[x+1][y] == "s":
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x+1][y] = grid[x+1][y].upper()
                                        pickupgem()
                                        break
                                else:
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x+1][y] = grid[x+1][y].upper()
                                        pickupgem()
                        except IndexError:
                                break
                else:
                        break

def slidejobbrale():
        while True:
                if not ismine():
                        try:
                                x = holalabda(grid)[0]
                                y = holalabda(grid)[1]
                                if grid[x+1][y+1]=="w":
                                        break
                                if x==n-1 or y==m-1:
                                        break
                                if grid[x+1][y+1] == "s":
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x+1][y+1] = grid[x+1][y+1].upper()
                                        pickupgem()
                                        break
                                else:
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x+1][y+1] = grid[x+1][y+1].upper()
                                        pickupgem()
                        except IndexError:
                                break
                else:
                        break

def slidebalrale():
        while True:
                if not ismine():
                        try:
                                x = holalabda(grid)[0]
                                y = holalabda(grid)[1]
                                if grid[x+1][y-1]=="w":
                                        break
                                if x==n-1 or y==0:
                                        break
                                if grid[x+1][y-1] == "s":
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x+1][y-1] = grid[x+1][y-1].upper()
                                        pickupgem()
                                        break
                                else:
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x+1][y-1] = grid[x+1][y-1].upper()
                                        pickupgem()
                        except IndexError:
                                break
                else:
                        break

def slidejobbrafel():
        while True:
                if not ismine():
                        try:
                                x = holalabda(grid)[0]
                                y = holalabda(grid)[1]
                                if grid[x-1][y+1]=="w":
                                        break
                                if x==0 or y==m-1:
                                        break
                                if grid[x-1][y+1] == "s":
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x-1][y+1] = grid[x-1][y+1].upper()
                                        pickupgem()
                                        break
                                else:
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x-1][y+1] = grid[x-1][y+1].upper()
                                        pickupgem()
                        except IndexError:
                                break
                else:
                        break

def slidebalrafel():
        while True:
                if not ismine():
                        try:
                                x = holalabda(grid)[0]
                                y = holalabda(grid)[1]
                                if grid[x-1][y-1]=="w":
                                        break
                                if x==0 or y==0:
                                        break
                                if grid[x-1][y-1] == "s":
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x-1][y-1] = grid[x-1][y-1].upper()
                                        pickupgem()
                                        break
                                else:
                                        grid[x][y] = grid[x][y].lower()
                                        grid[x-1][y-1] = grid[x-1][y-1].upper()
                                        pickupgem()
                        except IndexError:
                                break
                else:
                        break

def safebalra():
        e=1
        f=1
        while True:

                try:
                        x = holalabda(grid)[0]
                        y = holalabda(grid)[1]
                        if grid[x][y - f] == "w":
                                return True

                        if y==0:
                                return True
                        if grid[x][y - f] == "s":
                                return True
                        if grid[x][y-f] == "m":
                                return False
                        else:
                                f=f+1
                except IndexError:
                        return True

def safejobbra():
        e = 1
        f = 1
        while True:

                try:
                        x = holalabda(grid)[0]
                        y = holalabda(grid)[1]
                        if grid[x][y+f]=="w":
                                return True
                        if y==m-1:
                                return True
                        if grid[x][y+f] == "s":
                                return True
                        if grid[x][y+f] == "m":
                                return False
                        else:
                                f=f+1
                except IndexError:
                        return True


def safefel():
        e = 1
        f = 1
        while True:

                try:
                        x = holalabda(grid)[0]
                        y = holalabda(grid)[1]
                        if grid[x-e][y]=="w":
                                return True
                        if x==0:
                                return True
                        if grid[x-e][y] == "s":
                                return True

                        if grid[x-e][y] == "m":
                                return False
                        else:
                                e=e+1
                except IndexError:
                        return True


def safele():
        e = 1
        f = 1
        while True:

                try:
                        x = holalabda(grid)[0]
                        y = holalabda(grid)[1]
                        if grid[x+e][y]=="w":
                                return True
                        if x==n-1:
                                return True
                        if grid[x+e][y] == "s":
                                return True
                        if grid[x+e][y] == "m":
                                return False
                        else:
                                e=e+1
                except IndexError:
                        return True


def safejobbrale():
        e = 1
        f = 1
        while True:

                try:
                        x = holalabda(grid)[0]
                        y = holalabda(grid)[1]
                        if grid[x+e][y+f]=="w":
                                return True
                        if x==n-1 or y==m-1:
                                return True
                        if grid[x+e][y+f] == "s":
                                return True
                        if grid[x+e][y+f] == "m":
                                return False
                        else:
                                e=e+1
                                f=f+1
                except IndexError:
                        return True


def safebalrale():
        e = 1
        f = 1
        while True:

                try:
                        x = holalabda(grid)[0]
                        y = holalabda(grid)[1]
                        if grid[x+e][y-f]=="w":
                                return True
                        if x==n-1 or y==0:
                                return True
                        if grid[x+e][y-f] == "s":
                                return True
                        if grid[x+e][y-f] == "m":
                                return False
                        else:
                                e = e + 1
                                f = f + 1
                except IndexError:
                        return True


def safejobbrafel():
        e = 1
        f = 1
        while True:

                try:
                        x = holalabda(grid)[0]
                        y = holalabda(grid)[1]
                        if grid[x-e][y+f]=="w":
                                return True
                        if x==0 or y==m-1:
                                return True
                        if grid[x-e][y+f] == "s":
                                return True
                        if grid[x-e][y+f] == "m":
                                return False
                        else:
                                e = e + 1
                                f = f + 1

                except IndexError:
                        return True


def safebalrafel():
        e = 1
        f = 1
        while True:

                try:
                        x = holalabda(grid)[0]
                        y = holalabda(grid)[1]
                        if grid[x-e][y-f]=="w":
                                return True
                        if x==0 or y==0:
                                return True
                        if grid[x-e][y-f] == "s":
                                return True
                        if grid[x-e][y-f] == "m":
                                return False
                        else:
                                e = e + 1
                                f = f + 1
                except IndexError:
                        return True


#jobbra()
#balra()
#fel()
#le()
#jobbrafel()
#jobbrale()
#balrafel()
#balrale()
#fel()
#print(np.matrix(grid))
#print(gemsnum(grid))
#slide()
#print(safebalra())
#print(safejobbra())
#print(safele())
#print(safefel())
kor = 1

while True:


                if not ismine():
                        choiceList = []
                        if safejobbrafel():
                            choiceList.append(9)
                        if safejobbrale():
                            choiceList.append(3)
                        if safejobbra():
                            choiceList.append(6)
                        if safefel():
                            choiceList.append(8)
                        if safele():
                            choiceList.append(2)
                        if safebalrafel():
                            choiceList.append(7)
                        if safebalra():
                            choiceList.append(4)
                        if safebalrale():
                            choiceList.append(1)
                        print(kor, ". kör")
                        kor = kor + 1
                        print(gemsnum(grid), "gems left")
                        if choiceList==[]:
                            print("Zsákutca")
                            break
                        a=(random.choice(choiceList))
                        print(a)

                        if kor>5000:
                            print("túl sok kör, már úgyse lesz jó")
                            break
                        else:
                            if a==1:
                                    slidebalrale()

                            if a == 2:
                                    slidele()

                            if a == 3:
                                    slidejobbrale()

                            if a==4:
                                    slidebalra()

                            if a == 6:
                                    slidejobbra()

                            if a == 7:
                                    slidebalrafel()

                            if a==8:
                                    slidefel()

                            if a == 9:
                                    slidejobbrafel()


                        print()
                        print(np.matrix(grid))
                        print()
                        if gemsnum(grid)==0:
                                print("you won")
                                break
        #print("you are dead")

                else:
                        print("you are dead")
                        break



'''while True:
        try:
                if not ismine():
                        print(gemsnum(grid), "gems left")
                        a=int(input("Move?"))
                        if a==1:
                                slidebalrale()
                        if a == 2:
                                slidele()
                        if a == 3:
                                slidejobbrale()
                        if a==4:
                                slidebalra()
                        if a == 6:
                                slidejobbra()
                        if a == 7:
                                slidebalrafel()
                        if a==8:
                                slidefel()
                        if a == 9:
                                slidejobbrafel()
                        if a==0 or a==5:
                                print("surrender")
                                break
                        print()
                        print(np.matrix(grid))
                        print()
                        if gemsnum(grid)==0:
                                print("you won")
                                break
        #print("you are dead")

                else:
                        print("you are dead")
                        break
        except ValueError:
                print("wrongmove")'''







