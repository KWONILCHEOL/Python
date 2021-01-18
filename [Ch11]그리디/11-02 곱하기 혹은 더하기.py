s = input()
result = 0
for i in s:
  if result == 0:
    result += int(i) 
    continue
    
  if int(i) == 0:
    continue
  result *= int(i)

print(result)