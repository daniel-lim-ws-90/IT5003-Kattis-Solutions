import sys

size = 0
count = [0,0,0]


for line in sys.stdin:
    line = line.split()
    if len(line) == 1:
        size = int(line[0])    
    elif len(line) == 3:
        
        if str(line[0]) == 'J':
            
            count[0] += 1
        
        if str(line[1]) == 'J':
            
            count[1] += 1
        
        if str(line[2]) == 'J':
            
            count[2] += 1

count.sort()
print(count[0])
