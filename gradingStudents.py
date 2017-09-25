#!/bin/python3

import sys
def nextMult(grade):
    val = (grade // 5) * 5
    diff = val - grade
    
    if(diff > 0):
        return val
    else:
        return val + 5
    
    
def solve(grades):
    # Complete this function
    final = []
    for grade in grades:
        nextM = nextMult(grade)
        if grade < 38:
            final.append(grade)
        elif nextM - grade < 3:
            final.append(nextM)
        else:
            final.append(grade)
    return final
    

n = int(input().strip())
grades = []
grades_i = 0

for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
   
result = solve(grades)
print ("\n".join(map(str, result)))
