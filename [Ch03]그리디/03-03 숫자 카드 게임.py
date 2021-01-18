n, m = map(int,input().split())
result = 1
for i in range(n):
  arr = list(map(int,input().split()))
  result = max(result,min(arr))
print(result)