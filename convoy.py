import heapq

parameters = str(input())
parameters = parameters.split()


N = int(parameters[0])
maxCars = int(parameters[1])


cars = maxCars
stadiumArray = []
totalTime = 0
fastestDrivers = []

for i in range(N):
    
    fastestDrivers.append(int(input()))

fastestDrivers.sort()

destination = []

finalItem = None



while N > 0:

    if len(destination) == 0:

        item = fastestDrivers.pop(0)
        finalItem = (3*item,item)
        heapq.heappush(destination, finalItem)
        N -= min(N,5)
        maxCars -= 1

       

    elif maxCars == 0:

        
        item = destination[0]
        finalItem = (item[0] + 2*item[1], item[1])
        heapq.heapreplace(destination, finalItem)
        N -= min(N,4)

        
       

    elif fastestDrivers[0] <  destination[0][0]:

        item = fastestDrivers.pop(0)
        finalItem = (3*item,item)
        heapq.heappush(destination, finalItem)
        N -= min(N,5)
        maxCars -= 1
       
        

    else:

        item = destination[0]
        finalItem = (item[0] + 2*item[1], item[1])
        heapq.heapreplace(destination, finalItem)
        N -= min(N,4)

       
    
           

print(finalItem[0]-2*finalItem[1])
