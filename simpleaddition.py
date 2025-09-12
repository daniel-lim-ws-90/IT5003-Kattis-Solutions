num1 = str(input())
num2 = str(input())

num1 = num1[::-1]
num2 = num2[::-1]

length1 = len(num1)
length2 = len(num2)

carry = [0 for i in range(max(length1, length2)+ 1)]
final = []

for i in range(max(length1, length2)):
    
    if i < length1 and i < length2:
    
        char1 = int(num1[i])
        char2 = int(num2[i])
        char3 = carry[i]
    
        result = char1 + char2 + char3
        #print(result)
    
        if result > 9:
        
            carry[i+1] = 1
            final.append(result - 10)
    
        else:
        
            final.append(result)
    
    elif i < length1:
        
        char1 = int(num1[i])
        char3 = carry[i]
        result = char1 + char3
        #print(result)
        
        if result > 9:
        
            carry[i+1] = 1
            final.append(result - 10)
    
        else:
        
            final.append(result)
    
    elif i < length2:
        
        char2 = int(num2[i])
        char3 = carry[i]
        result = char2 + char3
        #print(result)
        
        if result > 9:
        
            carry[i+1] = 1
            final.append(result - 10)
    
        else:
        
            final.append(result)
        
        

if carry[-1] == 1:
    
    final.append(1)

final.reverse()

finalResult = []

for elt in final:

    character = str(elt)
    finalResult.append(character)



print(''.join(finalResult))
