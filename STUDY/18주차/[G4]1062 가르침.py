# [G4]1062 가르침
# https://www.acmicpc.net/problem/1062

import sys
import re
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]
visit = [False] * (26)
alpha = [1,3,4,5,6,7,9,10,11,12,14,15,16,17,18,20,21,22,23,24,25]

k -= 5
if k < 0:
    print(0)
    sys.exit()

for i in range(n):
    arr[i] = re.findall('[^antic]',arr[i])
_max = 0
cnt = 0
for x in combinations(alpha, k):
    for i in range(k):
        visit[x[i]] = True

    possible = 0
    for i in range(n):
        possible += 1
        for c in arr[i]:
            if visit[ord(c) - 97] == False:
                possible -= 1
                break

    if _max < possible:
        _max = possible

    for i in range(k):
        visit[x[i]] = False
print(_max)