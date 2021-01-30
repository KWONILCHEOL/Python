arr = [[0] * 10 for _ in range(10)]
for i in range(10):
  arr[i] = list(map(int, input().split()))

x,y=1,1
while True:
  if arr[x][y] == 0:
    arr[x][y] = 9
  if arr[x][y] == 2:
    arr[x][y] = 9
    break;

  if arr[x][y+1] != 1:
    y += 1
    continue
  
  if arr[x+1][y] != 1:
    x += 1
    continue
  
  break;

for i in range(10):
  print(*arr[i])
