import sys

n = int(sys.stdin.readline())
array = []
for i in range(n):
  array.append(int(sys.stdin.readline()))
array = sorted(array)

for x in array[::-1]:
  print(x, end = ' ')