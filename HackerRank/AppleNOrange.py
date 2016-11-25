#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apple = [(l if l > 0 else 0) for l in apple]
orange = [(l if l < 0 else 0) for l in orange]
countA = 0;
countO = 0;
for i in range(m):
    if (a+apple[i]) >= s and (a+apple[i]) <= t:
        countA += 1;
for i in range(n):
    if (b+orange[i]) >= s and (b+orange[i]) <= t:
        countO += 1;
print(countA)
print(countO)
