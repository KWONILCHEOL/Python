# [Ch16] 31 금광
# 열 이동하며 최대값 구하기

import sys
input = sys.stdin.readline
testCase = int(input())
for _ in range(testCase):
  n,m = map(int, input().split())
  arr = list(map(int,input().split()))

  dp = []
  for i in range(n):
    dp.append(arr[i * m : i * m + m])
  
  for j in range(1, m):
    for i in range(n):
      left = dp[i][j-1]
      left_up = 0
      left_down = 0
      if i > 0:
        left_up = dp[i-1][j-1]
      if i < n - 1:
        left_down = dp[i+1][j-1]
      
      dp[i][j] += max(left, left_up, left_down)
      
  #for j in range(1, m):
  #   for i in range(n):
  #     dp[i][j] = 0 + max(dp[i][j],(dp[i][j-1]+arr[i*m + j]))
  #     if i > 0:
  #       dp[i][j] = 0 + max(dp[i][j],(dp[i-1][j-1]+arr[i*m + j]))
  #     if i < n - 1:
  #       dp[i][j] = 0 + max(dp[i][j],(dp[i+1][j-1]+arr[i*m + j]))
  
  result = 0
  for i in range(n):
    result = max(result, dp[i][m-1])

  print(result)