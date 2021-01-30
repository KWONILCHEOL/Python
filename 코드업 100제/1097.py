arr = [[0] * 19 for _ in range(19)]

for i in range(19):
  arr[i] = list(map(int,input().split()))

n = int(input())
for _ in range(n):
  x,y = map(int, input().split())
  for i in range(19):
    arr[x-1][i] = 0 if arr[x-1][i] == 1 else 1
    arr[i][y-1] = 0 if arr[i][y-1] == 1 else 1

for i in range(19):
  print(*arr[i])
