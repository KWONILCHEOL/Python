# [G4]1261 알고스팟
# https://www.acmicpc.net/problem/1261

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(input().rstrip())

distance = [[INF] * (n) for _ in range(m)]
distance[0][0] = 0

q = []
heapq.heappush(q, (0,0,0))
while q:
    destory, x, y = heapq.heappop(q)
    if distance[x][y] < destory:
        continue

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx == m or ny == n:
            continue

        cost = destory + int(graph[nx][ny])
        if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q, (cost,nx,ny))

print(distance[m-1][n-1])