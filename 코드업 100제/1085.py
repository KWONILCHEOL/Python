h,b,c,s=map(int,input().split())
a = h * b * c * s
a //= 8
a /= pow(1024,2)
print("%.1f MB" % a)
