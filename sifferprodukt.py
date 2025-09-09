import sys

def generateProduct(num):
    
   
    while num > 9:
    
        numString = str(num)
        product = 1
    
        for elt in numString:
            
            if elt != '0':
                
                product = product*int(elt)
        
        num = product
    
    return num

 
for line in sys.stdin:
    data = int(line)
    print(generateProduct(data))
    