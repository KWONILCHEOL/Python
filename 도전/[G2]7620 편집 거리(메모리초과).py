# [G2]7620 편집 거리
# https://www.acmicpc.net/problem/7620
# 참고 : https://hsp1116.tistory.com/41

import sys
input = sys.stdin.readline

arr1 = ' ' + input().rstrip()
arr2 = ' ' + input().rstrip()

len1 = len(arr1)
len2 = len(arr2)

dp = [[0] * len2 for _ in range(len1)]
for i in range(len1):
  dp[i][0] = i
  
for j in range(len2):
  dp[0][j] = j

for i in range(1, len1):
  for j in range(1, len2):
    if arr1[i] == arr2[j]:
      dp[i][j] = dp[i-1][j-1]
    else:
      dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

# for i in range(len1):
#   for j in range(len2):
#     print(dp[i][j], end = ' ')
#   print()

q = [[len1-1,len2-1]]
x,y = q[0]
while x > 0 and y > 0:
  v = dp[x][y]
  if dp[x-1][y] == v-1:
    x = x-1
  elif dp[x][y-1] == v-1:
    y = y-1
  else:
    x,y = x-1,y-1
  q.append([x,y])

while x > 0:
  x -= 1
  q.append([x,y])

while y > 0:
  y -= 1
  q.append([x,y])
q.reverse()

for i in range(len(q)-1):
  x,y = q[i]
  nx,ny = q[i+1]
  mx, my = nx-x, ny-y
  if mx == 1 and my == 1:
    if dp[x][y] == dp[nx][ny]:
      print("c " + arr1[x+1])
    else:
      print("m " + arr2[y+1])
  elif mx == 1 and my == 0:
    if dp[x][y] == dp[nx][ny]:
      print("d " + arr1[x])
    else:
      print("d " + arr1[y+1])
  elif mx == 0 and my == 1:
    if dp[x][y] == dp[nx][ny]:
      print("a " + arr2[y])
    else:
      print("a " + arr2[y+1])