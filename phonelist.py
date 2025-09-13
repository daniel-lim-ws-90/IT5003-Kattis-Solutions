T = int(input())

for i in range(T):
    
    N = int(input())
    
    prefixDict = {}
    
    entryArray = []
    
    flag = False
    
    for j in range(N):
        
        entry = str(input())
        prefixDict[entry] = 1
        entryArray.append(entry)
    
    for elt in entryArray:
        
        length = len(elt)
        
        if flag == True:
            
            break
        
        for k in range(1,length):
            
            check = elt[:k]
            
            if  prefixDict.get(check) == 1:
                
                flag = True
                
                break
    
    if flag == False:
        
        print('YES')

    else:

        print('NO')
