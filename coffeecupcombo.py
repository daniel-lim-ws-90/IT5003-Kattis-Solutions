import sys

def drinkCoffee(strInput):
    
    remainder = 0
    count = 0
    
    for elt in strInput:
        
        if elt == '1':
            
            remainder = 2
            count += 1
        
        elif elt == '0':
            
            remainder -= 1
            
            if remainder > -1:
                
                count += 1
    
    return count
    

inputArray = []
for line in sys.stdin:
    data = str(line)
    inputArray.append(data)

print(drinkCoffee(str(inputArray[1])))