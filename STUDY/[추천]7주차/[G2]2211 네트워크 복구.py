# [G2]2211 네트워크 복구
# https://www.acmicpc.net/problem/2211

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int,input().split())
visit = [False] * (n+1)
arr = []
for _ in range(m):
    a,b,c = map(int, input().split())
    arr.append((a,b,c))
arr.sort(key = lambda x : x[2], reverse=True)

cnt = 0
ans = []
while arr:
    a,b,c = arr.pop()
    if visit[a] and visit[b]:
        continue

    ans.append((a,b))
    visit[a] = True
    visit[b] = True

print(len(ans))
for item in ans:
    print(*item)

# 4 5
# 1 2 1
# 1 4 4
# 1 3 2
# 4 2 2
# 4 3 3