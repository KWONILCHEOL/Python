a = int(input())
b = list(map(int,input().split()))
c = [0] * 23
for i in range(a):
  c[b[i] - 1] += 1
print(*c)
