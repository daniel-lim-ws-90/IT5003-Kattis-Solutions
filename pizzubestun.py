import sys

def pizza(array, size):
    
    array.sort()
    array = array[::-1]
    sumAns = 0
    
    for i in range(0,size,2):
        
        sumAns += array[i]
    
    return sumAns
    
size = 0
array = []

for line in sys.stdin:
    line = line.split()
    if len(line) == 1:
        size = int(line[0])    
    else:
        array.append(int(line[1]))

print(pizza(array, size))