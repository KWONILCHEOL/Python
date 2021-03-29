# [G3]20129 뒤집힌 계산기
# https://www.acmicpc.net/problem/20129

# 나누기 -> int(a/b)
import sys
import re
input = sys.stdin.readline

arr = list(map(int,input().split()))
x1 = input().rstrip()

p = re.compile("[0-9]+")
x2 = list(map(int, p.findall(x1)))
x2.reverse()

p = re.compile("[^0-9]")
x3 = p.findall(x1)
x3.reverse()

p = [[] for _ in range(4)]
p[arr[0] - 1] = '+'
p[arr[1] - 1] = '-'
p[arr[2] - 1] = '*'
p[arr[3] - 1] = '/'
print(x2)
print(x3)
print(p)
