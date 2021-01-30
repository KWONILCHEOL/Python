"""
f(n) = max(f(n-2), f(n-3)) + arr(n)
"""
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

d = [0] * (n + 1)
d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, n):
  d[i] = max(d[i-1], d[i-2] + arr[i])

print(d[n - 1])