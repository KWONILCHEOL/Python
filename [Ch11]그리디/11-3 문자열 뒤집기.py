s = input()

zeros = 0
ones = 0

now = '2'
for i in s:
  if i == now:
    continue
  now = i
  if i == '0':
    zeros += 1
  else:
    ones += 1

print(min(zeros,ones))