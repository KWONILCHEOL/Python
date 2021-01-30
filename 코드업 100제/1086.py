w,h,b=map(int,input().split())
a = w*h*b / 8 / pow(1024,2)
print("%.2f MB" % a)
