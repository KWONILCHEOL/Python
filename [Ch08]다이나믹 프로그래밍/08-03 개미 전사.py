"""
f(n) = max(f(n-2), f(n-3)) + arr(n)
"""
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

d = [0] * (n + 1)
d[0] = arr[0]
d[1] = arr[1]
d[2] = arr[0] + arr[2]

for i in range(3, n):
  d[i] = max(d[i-2], d[i-3]) + arr[i]

print(d[n - 1])