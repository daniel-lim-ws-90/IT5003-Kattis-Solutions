import sys

count = 0
for line in sys.stdin:
    data = str(line)
    
    for letter in data:
        
        if letter == 'u':
            
            count += 1
    
print(count)