from collections import deque

T = int(input())
strArray = []
endFlag = True
for i in range(T):
    
    strArray.append(str(input()))

for string in strArray:
    
    endFlag = True
    wordStack = deque()
    counter = 0
    for character in string:
        
        if character != '<' and character != '[' and character != ']' and endFlag == True:
            
            wordStack.append(character)
        
        elif character != '<' and character != '[' and character != ']' and endFlag == False:
            
           wordStack.insert(counter, character)
           counter += 1
        
        
        elif len(wordStack) > 0 and character == '<' and endFlag == True:
            
            wordStack.pop()
        
        elif counter > 0 and len(wordStack) > 0 and character == '<' and endFlag == False:

            counter -= 1
            del wordStack[counter]
            
        
        elif character == '[':
            
            endFlag = False
            counter = 0
            
        elif character == ']':
            
            endFlag = True
            counter = 0
        

    
    print(''.join(wordStack))