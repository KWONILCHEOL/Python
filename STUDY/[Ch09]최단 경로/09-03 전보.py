import sys
input = sys.stdin.readline

INF = int(1e9)
n,m,c = map(int,input().split())

city = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    
    
