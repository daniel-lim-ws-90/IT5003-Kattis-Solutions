N = int(input())
arrayNum = str(input())
arrayNum = arrayNum.split()
numArray = []

for x in arrayNum :
    
    numArray.append(int(x))

numArray.sort()



suM = 0
flag = False
for i in range(N-1):


    
    if  numArray[i] + 1 != numArray[i+1] and flag == False:
        
        suM += numArray[i]
        flag = False

    elif  numArray[i] + 1 != numArray[i+1] and flag == True:
        
        flag = False
    
    elif numArray[i] + 1 == numArray[i+1] and flag == False:
        
        flag = True
        suM += numArray[i]
        
    elif numArray[i] + 1 == numArray[i+1] and flag == True:
        
       flag = True
    

if numArray[N-1] != numArray[N-2]+1:

    suM += numArray[N-1]
    
print(suM)