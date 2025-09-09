import sys

count = 0
 
for line in sys.stdin:
    data = int(line)
    
    for i in range(1,data):
        
        if (i)*(i+1)*(i+2) < data:
            
            count += 1
        
        else:
            
            break
    

print(count)