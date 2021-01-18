n,m = map(int,input().split())
balls = list(map(int,input().split()))

arr = [0] * 11

for x in balls:
  arr[x] += 1

result = 0
for i in range(1,m+1):
  n -= arr[i]
  result += arr[i] * n
print(result)