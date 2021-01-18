n = int(input())
data = list(map(int,input().split()))
data.sort()

t = 1
for x in data:
  if t < x:
    break;
  t += x
print(t)

