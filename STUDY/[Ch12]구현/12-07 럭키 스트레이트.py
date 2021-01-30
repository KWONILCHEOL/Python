x = str(input())
length = len(x)
sum = 0
for i in range(length//2):
  sum += int(x[i]) - int(x[length-1-i])
  
print("LUCKY" if sum == 0 else "READY")