def binary_searchA(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -low

def binary_searchB(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
   
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -high


R = int(input())
strArray = str(input())
strArray = strArray.split()
numArray = []
numDict = {}

for elt in strArray:
    
    if numDict.get(int(elt)) == None:
        
        numDict[int(elt)] = 1
    
    else:
        
        numDict[int(elt)] += 1


#for key in numDict.keys():
    
    #numArray.append(key)

numArray = list(numDict.keys())
numArray.sort()

Q = int(input())

N = len(numArray)

max = 0
maxDict = {}

for key in numArray:
    
    max += numDict[key]
    maxDict[key] = max

for j in range(Q):
    
    inString = str(input())
    inString = inString.split()
    a = int(inString[0])
    b = int(inString[1])
    
    #index1 = -1
    #index2 = -1
    
    #arr1 = binary_search(numArray, a)
    #arr2 = binary_search(numArray, b)
    index1 = binary_searchA(numArray, a)
    index2 = binary_searchB(numArray, b)
    
    #for i in range(N):
        
        #if numArray[i] >= a:
            
            #index1 = i
            #break
    
    #for i in range(N):
        
        
        #if numArray[N-1-i] <= b:
            
            #index2 = N-1-i
            #break
    
    

    if a > numArray[-1] or b < numArray[0] :
        
        print(0)
        
        
    elif a == b:
        
        if index1 < 0:
            
            print(0)
        
        else: 
            
            print(numDict[numArray[abs(index1)]])
        
    else:
        
        #count = 0
        #for i in range(abs(index1), abs(index2)+1):
            
            #count += numDict[numArray[i]]
        
        #print(count)
        
        e = numDict[numArray[abs(index1)]]
        f = maxDict[numArray[abs(index1)]]
        g = maxDict[numArray[abs(index2)]]
        
        print(g-f+e)
