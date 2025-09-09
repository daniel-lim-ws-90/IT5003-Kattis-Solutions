N = int(input())
arrayString = str(input())
arrayString = arrayString.split()
numArray = []
for elt in arrayString:
    
    numArray.append(int(elt))

copyArray = numArray.copy()
numArray.sort(reverse=True)
subArray = []

for i in range(N):
    
    if numArray[N-1-i] != copyArray[i]:
        
        subArray.append(copyArray[i])

length = len(subArray)

flag = True

for i in range(length-1):
    
    if subArray[i] < subArray[i+1]:
        
        flag = False
        break

if flag == False:
    
    print('No')

elif flag == True:
    
    print('Yes')
        