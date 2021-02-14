from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
G = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    G[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    cnt = 0
    while q:
        cnt += 1
        length = len(q)
        for _ in range(length):
            now = q.popleft()
            result.append((cnt, now))

            for i in G[now]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)


    print(*result)

topology_sort()

# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4