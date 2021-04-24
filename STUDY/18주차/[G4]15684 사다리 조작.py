# [G4]15684 사다리 조작
# https://www.acmicpc.net/problem/15684

import sys
from itertools import combinations
input = sys.stdin.readline

def check():
    diff = 0
    for i in range(1, n + 1):
        x = i
        for j in range(1, h + 1):
            if ladder[j][x]:
                x+= 1
            elif ladder[j][x-1]:
                x-= 1
        if x != i:
            diff += 1

    return diff

def check2():
    for a,b in temp1:
        if (a,b-1) in temp1 or (a,b+1) in temp1:
            return False

    return True
n,m,h = map(int,input().split())
ladder = [[0] * (n+2) for _ in range(h+2)]

temp1 = []
for _ in range(m):
    a,b = map(int, input().split())
    ladder[a][b] = 1
    temp1.append((a,b))

du = check()
if du == 0:
    print("0")
    sys.exit()

if du > 6:
    print("-1")
    sys.exit()

temp0 = []
for i in range(1, h + 1):
    for j in range(1, n):
        if ladder[i][j] == 0 and ladder[i][j-1] == 0 and ladder[i][j+1] == 0:
            temp0.append((i,j))

for a, b in temp0:
    temp1.append((a,b))
    if check2() == False:
        temp1.remove((a,b))
        continue

    ladder[a][b] = 1
    if check() == 0:
        print("1")
        sys.exit()
    ladder[a][b] = 0
    temp1.remove((a, b))

for a, b in combinations(temp0, 2):
    temp1.append(a)
    temp1.append(b)
    if check2() == False:
        temp1.remove(a)
        temp1.remove(b)
        continue

    ladder[a[0]][a[1]] = 1
    ladder[b[0]][b[1]] = 1
    if check() == 0:
        print("2")
        sys.exit()
    ladder[a[0]][a[1]] = 0
    ladder[b[0]][b[1]] = 0
    temp1.remove(a)
    temp1.remove(b)

for a, b, c in combinations(temp0, 3):
    temp1.append(a)
    temp1.append(b)
    temp1.append(c)
    if check2() == False:
        temp1.remove(a)
        temp1.remove(b)
        temp1.remove(c)
        continue

    ladder[a[0]][a[1]] = 1
    ladder[b[0]][b[1]] = 1
    ladder[c[0]][c[1]] = 1
    if check() == 0:
        print("3")
        sys.exit()
    ladder[a[0]][a[1]] = 0
    ladder[b[0]][b[1]] = 0
    ladder[c[0]][c[1]] = 0

    temp1.remove(a)
    temp1.remove(b)
    temp1.remove(c)
print("-1")