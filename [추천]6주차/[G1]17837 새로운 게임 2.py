# [G1]17837 새로운 게임 2
# https://www.acmicpc.net/problem/2568

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = [0] + [0] * n
for _ in range(n):
  a,b = map(int,input().split())
  arr[a] = b

dp = []
for i in range(n):
  for x in arr:
    index = bisect_left(dp, x)

    if index < len(dp):
      dp[index] = x
    else:
      dp.append(x)

# dp = [1] * n
# for i in range(1,n):
#   for j in range(0,i):
#     if arr[j] < arr[i]:
#       dp[i] = max(dp[i], dp[j] + 1)
# print(n - max(dp))

print(n - len(dp))

#dp[n]은 총 n개 선택했을 때 감소하는 최대 숫자