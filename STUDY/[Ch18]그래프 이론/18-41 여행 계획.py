import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def topology_sort():
    result = deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for x in graph[now]:
            result[x] = max(result[x], result[now] + time[x])
            indegree[x] -= 1
            if indegree[x] == 0:
                q.append(x)
        print(result)
        print(time)

    print(*result[1:], sep='\n', end='')

n = int(input())
graph = [[] for i in range(n+1)]
time = [0] * (n+1)

indegree = [0] * (n+1)
for i in range(1, n+1):
    arr = list(map(int,input().split()))
    time[i] = arr[0]
    for x in arr[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

topology_sort()

# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1