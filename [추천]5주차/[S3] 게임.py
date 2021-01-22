# [S3] 게임
# https://www.acmicpc.net/problem/1072
# 시간 복잡도 : O(logn)

def get_rate(x,y):
  return int(y/x*100)

x, y = map(int, input().split())
z = get_rate(x,y)

if z >= 99:
  print(-1)
else:
  lo = 1
  hi = int(1e9)
  while lo <= hi:
    mid = (lo + hi) // 2
    nx, ny = x + mid, y + mid
    nz = get_rate(nx,ny)
    print(z, nz, lo,mid,hi)
    if z == nz:
      lo = mid + 1
    else:
      hi = mid - 1
  print(lo)