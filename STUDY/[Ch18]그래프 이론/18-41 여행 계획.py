import sys
input = sys.stdin.readline

def find_parent(p, x):
    while p[x] != x:
        p[x], x = p[p[x]], p[x]
    return x

def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

def answer(p):
    arr = list(map(int, input().split()))
    temp = find_parent(parent, arr[0])
    for x in arr:
        if temp != find_parent(parent, x):
            return "NO"

    return "YES"

n, m = map(int,input().split())
G = [[] for _ in range(n)]
parent = [i for i in range(n)]

for i in range(n):
    G[i] = (list(map(int, input().split())))

for i in range(n):
    for j in range(i+1, n):
        if G[i][j] == 1:
            union_parent(parent,i,j)

print(answer(parent), end='')

# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3