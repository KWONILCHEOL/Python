# [S1]2293 동전 1
# https://www.acmicpc.net/problem/2293
import sys
from bisect import bisect_left
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
dp = [1] + [0] * k3
print(len(dp))
for _ in range(n):
    arr.append(int(input()))

for j in range(n):
    i = 0
    while i < k:
        
for i in range(1, k+1):
    for j in range(n):
        if (i - arr[j]) >= 0:
            dp[i] += dp[i-arr[j]]


print(dp[k])

