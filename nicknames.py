nameNum = int(input())
nameArray = []

for i in range(nameNum):
    
    name = str(input())
    nameArray.append(name)

nickNum = int(input())
nickArray = []

for i in range(nickNum):
    
    nick = str(input())
    nickArray.append(nick)

nameDict = {}

for name in nameArray:
    
    length = len(name)
    
    for i in range(1,length+1):
        
        elt = name[:i]
        
        if nameDict.get(elt) == None:
            
            nameDict[elt] = [name]
        
        else:
            
            nameDict[elt].append(name)

for nickName in nickArray:
    
    if nameDict.get(nickName) != None:
        
        print(len(nameDict[nickName]))
    
    else:
        
        print(0)