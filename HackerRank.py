""" Programs for HackerRank
"""
"""
    LeftRotate
    n, d = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))

    d %= n
    print(*(arr[d:] + arr[:d]))
"""
import sys
buff = [1,2,3]
count = 0
while True:
    line = sys.stdin.readline()    
    buff[count] = line.split(' ')
    if count == 2:
        break
    count += 1

n =int(buff[0][0])
d = int(buff[0][1])
k = d
arr = list(buff[1])
larr = arr[:]

t0 = 0
z0 = -(d)

for i in range(int(n)):
    larr[z0] = arr[t0]
    z0 += 1
    t0 += 1
    if z0 == 0:
        for j in range(n-d):          
            larr[j] = arr[k]
            k += 1
        break
        
for k in larr:
    sys.stdout.write(k)
    sys.stdout.write(' ')

"""
    Sparse Array
"""
import sys
count = 0
string = []
num = []

while True:    
    s = sys.stdin.readline()
    s = s.strip()
    if s.isdecimal():
        num.append(int(s))
        continue
    if s == '':        
        break
    string.append(s)
    
query = list(x.strip() for x in string[-(num[1]):])
string =list(x.strip() for x in string[:(num[0])])

num = query[:]

track = 0

for i in query:
    for j in string:
        if i == j:
            track += 1
            num[count] = track
        else:
            if str(num[count]).isalpha():
                num[count] = 0        
    count += 1
    track = 0

for i in num:
    sys.stdout.write(str(i))
    sys.stdout.write('\n')


    
