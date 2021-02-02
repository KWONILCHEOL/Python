#시작 지점에서 n번 탐색(가장 가까우면서 방문하지 않은 노드 찾기)
#찾은 노드를 거쳐가는(n번) 것이 빠른지 확인

import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input(). split())
start = int(input())
graph = [[]for _ in range(n+1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]

            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])