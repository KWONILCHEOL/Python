n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort(reverse = True)
print(arr[0] * (m - (m // (k+1))) + arr[1] * (m // (k+1)))