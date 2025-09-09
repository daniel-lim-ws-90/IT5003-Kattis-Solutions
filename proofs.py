

def proof():

    n = int(input())

    trueDict = {}

    #globalFlag = True
    
    for i in range(n):
        
        sentence = str(input())
        
        sentence = sentence.split('->')
        
        if sentence[0] == '':
            
            trueDict[sentence[1].strip()] = True
    
            #print(sentence[1])
        
        else:
            
            premise = sentence[0].split()
    
            #print(premise)
            
            for elt in premise:
                
                if trueDict.get(elt) == None:
                    
                    #globalFlag = False
                    
                    print(i+1)
                    
                    return
                
            
            trueDict[sentence[1].strip()] = True
    
    
    #print(trueDict)
    #if globalFlag == True:
        
    print('correct')


proof()
                
                
