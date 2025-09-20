import heapq

parameters = str(input())
parameters = parameters.split()

n = int(parameters[0])
k = int(parameters[1])

#serverArray = []
timeQ = []
lengthQ = []
#newQ = []
first = int(input()) + 1000
#newQ.append(first)
#serverArray.append(newQ)

timeQ.append((first, 0))
lengthQ.append((1,0))
count = 1


for i in range(n-1):
    
    timeStamp = int(input())
    allocated = False
    
    timeElt = timeQ[0]
    lengthElt = lengthQ[0]
    
    if timeStamp >= timeElt[0]:
            
            #heapq.heapreplace(serverArray[timeElt[1]], timeStamp + 1000)
            allocated = True
            heapq.heapreplace(timeQ, (timeStamp + 1000,  timeElt[1]))
    
    
    if allocated == False:
            
            if len(timeQ) < count*k:

                heapq.heapreplace(lengthQ, (lengthElt[0] + 1,  lengthElt[1]))
                heapq.heappush(timeQ, (timeStamp + 1000,  lengthElt[1]))
                allocated = True
                
    
    if allocated == False:

        
        heapq.heappush(timeQ, (timeStamp + 1000,  count))
        heapq.heappush(lengthQ, (1,  count))
        count += 1
        
       


print(count)
