import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
  data = int(input())
  heapq.heappush(heap, data)

result = 0
while len(heap) != 1:
  a = heapq.heappop(heap)
  b = heapq.heappop(heap)
  x = a + b
  result += x
  heapq.heappush(heap, x)
  
print(result)