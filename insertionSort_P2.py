import sys
n = int(input())
arr = [int(i) for i in (input().strip().split())]
curPos = 0

for j in range(n):
    for i in range(j):
        if  arr[i] > arr[j]:       
            dum = arr[i]
            arr[i] = arr[j]
            arr[j] = dum
    if(j > 0):
        for i in arr:
            sys.stdout.write(str(i)+" ")
        print()  
