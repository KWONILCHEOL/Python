# [G3]10800 컬러볼
# https://www.acmicpc.net/problem/10800

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
ans = [0] * (n)
color = {}

balls = [[i] + list(map(int, input().split())) for i in range(n)]
balls.sort(key=lambda x:(x[2]))

answer = defaultdict(int)
_sum = defaultdict(int)

total = 0
i,j = 0,0
for i in range(n):
    while balls[j][2] < balls[i][2]:
        total += balls[j][2]
        _sum[balls[j][1]] += balls[j][2]
        j += 1
    answer[balls[i][0]] = total - _sum[balls[i][1]]

for i in range(n):
    print(answer[i])