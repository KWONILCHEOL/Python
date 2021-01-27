# [Ch16] 35 못생긴 수
"""
 ┌1  2  3  4  5  6  8  9  10
2│   4  6  8  10 12    
3│   6  9  12
5│   10 15
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * n
arr[0] = 1

i2 = i3 = i5 = 0
next2, next3, next5 = 2,3,5

for i in range(1,n):
  arr[i] = min(next2,next3,next5)

  print(arr, next2, next3, next5)
  if arr[i] == next2:
    i2 += 1
    next2 = arr[i2] * 2
  if arr[i] == next3:
    i3 += 1
    next3 = arr[i3] * 3
  if arr[i] == next5:
    i5 += 1
    next5 = arr[i5] * 5

print(arr[n-1])