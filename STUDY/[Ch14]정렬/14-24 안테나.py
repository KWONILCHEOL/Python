import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rstrip().split()))
arr = sorted(arr)
print(arr[(n-1)//2])