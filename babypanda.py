import sys
import math

n, m = map(int, input().split())
count = 0
    
while m > 0:
        
    index = math.log2(m)
    x = math.floor(index)
    m = m - 2**x
    count += 1

print(count)
