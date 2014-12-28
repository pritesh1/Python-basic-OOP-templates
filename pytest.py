from math import *

b = int(raw_input())
for k in range(0,b):
    n = int(raw_input())
    root1 = sqrt(5 * n**2 + 4)
    root2 = sqrt(5 * n**2 - 4)
    isFibo = root1 % 1 == 0 or root2 % 1 == 0


for k in range(b):
    
    if(isFibo):
        print "IsFibo"

    else:
        print "IsNotFibo"

