import sys
input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
  cards.append(int(input()))
cards.sort(reverse = True)

length = len(cards)
answer = 0
for x in cards:
  answer = answer + x * (length - 1)
  length = length - 1
  cards.pop()

print(answer)