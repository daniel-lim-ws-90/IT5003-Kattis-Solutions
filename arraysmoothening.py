import heapq

parameters = str(input())
parameters = parameters.split()



array = str(input())
array = array.split()

N = int(parameters[0])
K = int(parameters[1])

freqDict = {}

arrayHeap = []

for elt in array:
    
    if freqDict.get(elt) == None:
        
        freqDict[elt] = -1
    
    else:
        
        freqDict[elt] -= 1


for key in freqDict.keys():
    
    elt = (freqDict[key], key)
    
    arrayHeap.append(elt)


heapq.heapify(arrayHeap)



while K > 0:

    comparison = min(arrayHeap[1][0], arrayHeap[2][0])

    difference = arrayHeap[0][0] - comparison -1

    takeAway =  min(abs(difference), K)

    K -= takeAway

    item = (arrayHeap[0][0] + takeAway, arrayHeap[0][1] )

    heapq.heapreplace(arrayHeap, item)

print(abs(arrayHeap[0][0]))
        

