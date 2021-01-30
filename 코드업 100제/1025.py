a = input()
length = len(a)
for i in range(length):
  print('[' + a[i] + '0' * (length - 1 - i) +']')