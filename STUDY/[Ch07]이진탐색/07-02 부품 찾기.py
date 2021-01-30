# [Ch07] 02 부품 찾기
# 시간 복잡도 : O(1), O(1), O((M+N)logN)

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  
  return None

import sys
input = sys.stdin.readline  

n = int(input().rstrip())
parts = list(map(int,input().rstrip().split()))

m = input().rstrip()
want = list(map(int,input().rstrip().split()))


#O(1)
arr = [[False] for _ in range(1000001)]
for x in parts:
  arr[x] = True

for x in want:
  print("yes" if arr[x] == True else "no",end = ' ')
print()

#O(1)
arr = set(map(int, parts))
for x in want:
  print("yes" if x in arr else "no",end = ' ')
print()

#O((M+N)logN)
parts.sort()
for x in want:
  result = binary_search(parts, x, 0, n -1)
  print("yes" if result != None else "no",end = ' ')
print()