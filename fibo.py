# FIB
from collections import defaultdict

for i in range(int(input().strip())):
    F0,F1,Fn =  input().split(' ')
    F0 = int(F0)
    F1 = int(F1)
    Fn = int(Fn)
    for k in range(Fn-1):
        F = F1 + F0 
        F0 = F1
        F1 = F
    print(F1)
        
