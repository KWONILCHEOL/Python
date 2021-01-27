# [Ch16] 34 병사 배치하기
# [S2]18353 퇴사
# https://www.acmicpc.net/problem/18353
# 다이나믹 프로그래밍, 가장 긴 증가하는 부분 수열

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
dp = []

for x in arr[::-1]:
  index = bisect_left(dp, x)

  if index < len(dp):
    dp[index] = x
  else:
    dp.append(x)

print(n - len(dp))

#dp[n]은 총 n개 선택했을 때 증가하는 최소 숫자