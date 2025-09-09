import sys

inputArray = []
length = int(input())
for i in range(length):
    data = str(input())
    inputArray.append(data)


controlGroup = 0
vaccGroup = 0
controlGroupA = 0
controlGroupB = 0
controlGroupC = 0
vaccGroupA = 0
vaccGroupB = 0
vaccGroupC = 0

for i in range(0, length):
    
    if inputArray[i][0] == 'N':
        
        controlGroup += 1
    
    if inputArray[i][0] == 'Y':
        
        vaccGroup += 1
    
    if inputArray[i][0] == 'N' and inputArray[i][1] == 'Y':
        
        controlGroupA += 1 
    
    if inputArray[i][0] == 'N' and inputArray[i][2] == 'Y':
        
        controlGroupB += 1
    
    if inputArray[i][0] == 'N' and inputArray[i][3] == 'Y':
        
        controlGroupC += 1
    
    if inputArray[i][0] == 'Y' and inputArray[i][1] == 'Y':
        
        vaccGroupA += 1
    
    if inputArray[i][0] == 'Y' and inputArray[i][2] == 'Y':
        
        vaccGroupB += 1
    
    if inputArray[i][0] == 'Y' and inputArray[i][3] == 'Y':
        
        vaccGroupC += 1

if vaccGroupA/vaccGroup >= controlGroupA/controlGroup :
    
    print('Not Effective')

else:
    
    print(round(100 - 100*(vaccGroupA/vaccGroup)/(controlGroupA/controlGroup),2))

if vaccGroupB/vaccGroup >= controlGroupB/controlGroup :
    
    print('Not Effective')

else:
    
    print( round(100 - 100*(vaccGroupB/vaccGroup)/(controlGroupB/controlGroup),2)) 
    

if vaccGroupC/vaccGroup >= controlGroupC/controlGroup :
    
    print('Not Effective')

else:
    
    print(round(100 - 100*(vaccGroupC/vaccGroup)/(controlGroupC/controlGroup),2)) 