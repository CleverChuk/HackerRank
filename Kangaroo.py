
import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
count = 0
while True:
    if(x1 == x2):
        print("YES")
        break
    if count > 10000:
        print("NO")
        break
    x1 = v1 + x1
    x2 = v2 + x2
    count += 1
