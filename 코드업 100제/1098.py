w,h = map(int, input().split())
arr = [[0] * h for _ in range(w)]
n = int(input())
for _ in range(n):
  l,d,x,y = map(int, input().split())
  arr[x-1][y-1] = 1
  for i in range(l - 1):
    if d == 0:
      y += 1
    elif d == 1:
      x += 1
    arr[x-1][y-1] = 1

for i in range(w):
  print(*arr[i])
