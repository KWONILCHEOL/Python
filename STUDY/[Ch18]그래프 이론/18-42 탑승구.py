import sys
input = sys.stdin.readline

def find_parent(p, x):
    while p[x] != x:
        p[x], x = p[p[x]], p[x]
    return x

P = int(input())
G = int(input())
parent = [i for i in range(P+1)]
arr = []
for _ in range(G):
    arr.append(int(input()))

ans = 0
for x in arr:
    p = find_parent(parent, x)
    if p == 0:
        break
    ans += 1
    parent[p] = find_parent(parent, p-1)

print(ans)

# 4
# 6
# 2
# 2
# 3
# 3
# 4
# 4