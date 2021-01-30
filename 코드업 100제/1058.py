a,b = map(int, input().split())
x,y = bool(a), bool(b)
print(int(not (x or y)))
