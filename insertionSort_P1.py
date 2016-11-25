import sys
n = int(input())+1
arr = [int(i) for i in (input().strip().split())]
curPos = 0
e = arr[-1]

for i in range(-2,-n,-1):
    count += 1
    if e < arr[i]:
        curPos = i
        dum = arr[i]
        arr[i] = dum
        arr[i+1] = dum
        for i in arr:
            sys.stdout.write(str(i)+" ")
        print()    
arr[curPos] = e

for i in arr:
    sys.stdout.write(str(i)+" ")
