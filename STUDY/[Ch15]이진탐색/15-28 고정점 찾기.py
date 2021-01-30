# [Ch15] 28 고정점 찾기
# 시간 복잡도 : O(logN)

import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

start = 0
end = n-1
ans = -1
while start <= end:
  mid = (start + end) // 2
  if arr[mid] == mid:
    ans = mid
    break
  elif arr[mid] < mid:
    start = mid + 1
  elif arr[mid] > mid:
    end = mid - 1

print(ans)