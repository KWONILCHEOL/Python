"""
방법 1 : 바텀업
방법 2 : 탑다운(BFS)
"""
import sys
x = int(sys.stdin.readline())

bu = [0] * (x + 1)

for i in range(2, x + 1):
  bu[i] = bu[i-1] + 1
  if i%2 == 0:
    bu[i] = min(bu[i], bu[i//2] + 1)
  if i%3 == 0:
    bu[i] = min(bu[i], bu[i//3] + 1)
  if i%5 == 0:
    bu[i] = min(bu[i], bu[i//5] + 1)

print(bu[x])

td = [x] * (x + 1)
td[x] = 0
que = set([x])
while que:
  a = que.pop()
  if td[a-1] > td[a] + 1:
    td[a-1] = td[a] + 1
    que.add(a-1)

  if a%2 == 0:
    if td[a//2] > td[a] + 1:
      td[a//2] = td[a] + 1
      que.add(a//2)

  if a%3 == 0:
    if td[a//3] > td[a] + 1:
      td[a//3] = td[a] + 1
      que.add(a//3)

  if a%5 == 0:
    if td[a//5] > td[a] + 1:
      td[a//5] = td[a] + 1
      que.add(a//5)

print(td[1])