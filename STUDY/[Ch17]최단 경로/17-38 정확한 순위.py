# [Ch17] 38 정확한 순위
# 플로이드 와샬

# graph1[a][b]  정방향
# graph2[b][a]  반대방향
# 기준점에서 양 방향의 개수를 계산해도 가능

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]
distance = [[] * (n+1) for _ in range(n+1)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != 0 or graph[j][i] != 0:
            count += 1
    if count == n - 1:
        result += 1

for i in range(1, n+1):
    print(*graph[i][1:])

print(result)

# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4