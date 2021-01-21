# [Ch07] 03 떡볶이 떡 만들기
# 시간 복잡도 : O(N + NlogN)
'''
시작점은 (가장 긴 떡의 길이 - 요청한 떡의 길이)
마지막은 (가장 긴 떡의 길이)로 이진탐색 한다.
(단, 시작점이 0보다 작으면 시작점은 0부터 시작한다.)
'''
import sys
input = sys.stdin.readline  


def getLength(arr, mid):
  return sum(x - mid for x in arr if x > mid)

def binary_search(arr, target, start, end):
  answer = 0
  while start <= end: #O(logN)
    mid = (start + end) // 2
    x = getLength(arr,mid)  #O(N)
    if x < target:
      end = mid - 1
    elif x > target:
      answer = max(answer, mid)
      start = mid + 1
    else:
      return mid
  
  return answer

n, m = map(int,input().rstrip().split())
rc = list(map(int,input().rstrip().split()))

end = max(rc) #O(N)
start = max(0, end - m)
print(binary_search(rc,m,start,end))