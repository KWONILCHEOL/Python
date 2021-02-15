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
P = [i for i  in range(n+1)]

for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union_parent(parent, a, b)
    else:
        print("YES" if find_parent(parent, a) == find_parent(parent, b) else "NO")
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
