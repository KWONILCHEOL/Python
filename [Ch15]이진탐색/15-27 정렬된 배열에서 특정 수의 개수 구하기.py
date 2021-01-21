# [Ch15] 27 정렬된 배열에서 특정 수의 개수 구하기
# 강의

import sys
input = sys.stdin.readline

from bisect import bisect_left, bisect_right

def count_by_range(arr, left_value, right_value):
  right_index = bisect_right(arr, right_value)

  left_index = bisect_left(arr,left_value)

  return right_index - left_index

n, x = map(int,input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

count = count_by_range(arr,x,x)
if count == 0:
  print(-1)
else:
  print(count)