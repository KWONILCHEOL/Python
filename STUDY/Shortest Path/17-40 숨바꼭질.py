# [Ch17] 40 숨바꼭질
# [S1]6118 숨바꼭질
# https://www.acmicpc.net/problem/6118

import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = []
start = 1
distance[start] = 0
heapq.heappush(q, (0, start))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

_max = max(x for x in distance if x != 1e9)
#max_distance = max(filter(lambda x : x != 1e9, distance))
print(distance.index(_max), _max, distance.count(_max))


# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2