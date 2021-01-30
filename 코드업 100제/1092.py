from math import gcd

def lcm(x, y):
  return x * y // gcd(x,y)

a,b,c = map(int, input().split())
print(lcm(lcm(a,b),c))
