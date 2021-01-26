"""
f(n) = f(n-1) + f(n-2) * 2
f(0) = 1
f(1) = 1
"""
import sys
input = sys.stdin.readline
n = int(input())
d = [0] * (n + 1)
d[0] = 1
d[1] = 1
for i in range(2, n+1):
  d[i] = d[i-1] + (d[i-2] * 2) % 796796

print(d[n])