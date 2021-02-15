import sys
input = sys.stdin.readline

def find_parent(parent, x):
    while parent[x] != x:
        parent[x], x = parent[parent[x]], parent[x]
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n)]

edges = []
total = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c,a,b))
    total += c

edges.sort()
for c,a,b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total -= c

print(total)

# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11