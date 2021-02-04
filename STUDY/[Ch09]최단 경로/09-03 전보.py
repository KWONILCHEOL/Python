import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n, m, start = map(int, input().split())
city = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    city[x].append((y, z))


q = []
distance[start] = 0
heapq.heappush(q, (0,start))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue

    for x in city[now]:
        cost = dist + x[1]
        if cost < distance[x[0]]:
            distance[x[0]] = cost
            heapq.heappush(q, (cost, x[0]))



count = len([d for d in distance if 0 < d < 1e9])
max_distance = max([d for d in distance if d < 1e9])
print(count, max_distance)

# 3 2 1
# 1 2 4
# 1 3 2
