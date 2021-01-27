# [Ch16] 36 편집 거리
# 

import sys
input = sys.stdin.readline

arr1 = input().rstrip()
arr2 = input().rstrip()

len1 = len(arr1) + 1
len2 = len(arr2) + 1
dp = [[0] * len2 for _ in range(len1)]
for i in range(len1):
  dp[i][0] = i
  
for j in range(len2):
  dp[0][j] = j

for a1 in arr1:
  for a2 in arr2:
    if a1 == a2:
      dp[i][j] = dp[i-1][j-1]
    else:
      dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

print(dp)
print(dp[len1-1][len2-1])

# for i in range(len1 + 1):
#   for j in range(len2 + 1):
