# [Ch16] 32 정수 삼각형
# [S1]1932 정수 삼각형
# https://www.acmicpc.net/problem/1932
# 다이나믹 프로그래밍 DP

import sys
input = sys.stdin.readline
n = int(input())
dp = []
for _ in range(n):
  dp.append(list(map(int, input().split())))

for i in range(n-1, 0, -1):
  for j in range(i):
    dp[i-1][j] = max(dp[i][j], dp[i][j+1]) + dp[i-1][j]

print(dp[0][0])