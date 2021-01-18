import sys

n = int(sys.stdin.readline())
array = []
for i in range(n):
  array.append(sys.stdin.readline().rstrip().split())

array = sorted(array, key = lambda x : x[1])
for x in array:
  print(x[0], end = ' ')