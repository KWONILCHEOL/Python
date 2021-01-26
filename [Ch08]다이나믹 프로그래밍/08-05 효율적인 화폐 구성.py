"""
f(n) = max(f(n-x1), f(n-x2), ..., f(n-xn)) + 1
"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = [0] + [10001] * m
arr = []
for i in range(n):
  arr.append(int(input()))
for i in range(1, m + 1):
  for j in arr:
    if i - j >= 0:
      d[i] = min(d[i], d[i-j] + 1)

print(-1 if d[m] == 10001 else d[m])