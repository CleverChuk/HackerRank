def quickSort(ar):
    left = []
    right = []
    
    if len(ar) < 2:
        return ar
    p = ar[0]
    for i in ar:
        if i < p:
            left.append(i)
        if i > p:
            right.append(i)
            
    arr = quickSort(left) +[p]+ quickSort(right)
    print(" ".join(map(str,arr)))    
    return arr

_ = input()
ar = [int(i) for i in input().strip().split()]
ar = quickSort(ar)
