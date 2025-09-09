import sys

count = 0
dictCount = {}
finalCount = 0
 
for line in sys.stdin:
    data = str(line)
    
    length = len(data)
    
    
    for i in range(length):
        
        if data[i] == '>':
            
            count += 1
            
        
        elif data[i] == '<':
            
            dictCount[i] = count


for item in dictCount.keys():
    
    finalCount += dictCount[item]

print(finalCount)