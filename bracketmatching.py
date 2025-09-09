from collections import deque


N = int(input())
strIn = str(input())
strArray = []

for elt in strIn:

    strArray.append(elt)

stack = deque()
valid = True
#print(strArray)

for elt in strArray:
    
    if elt == '(':
       
        stack.append(elt)
        #print(len(stack))
    
    elif elt == '[':
        
        stack.append(elt)
        #print(len(stack))
        
    elif elt == '{':
        
        stack.append(elt)
        #print(len(stack))

    elif elt == ')':
        #print(len(stack))
        if len(stack) > 0:
            result = stack.pop()
            if result != '(':
                valid = False
                break
        
        else:
            
            valid = False
            break
        
    
    elif elt == ']':
        #print(len(stack))
        if len(stack) > 0:
            result = stack.pop()
            if result != '[':
                valid = False
                break
        
        else:
            
            valid = False
            break  
    
    
    elif elt == '}':
        #print(len(stack))
        if len(stack) > 0:
            result = stack.pop()
            if result != '{':
                valid = False
                break
        
        else:
            
            valid = False
            break  

#print(stack)
if len(stack) > 0:
    
    valid = False

if valid == True:
    
    print('Valid')

elif valid == False:
    
    print('Invalid')
