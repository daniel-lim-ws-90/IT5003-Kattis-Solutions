def buslines():
    
    parameters = str(input())
    parameters = parameters.split()
    
    totalStations = int(parameters[0])
    totalBuslines = int(parameters[1])
    
    
    distinctHash = [False for i in range((totalStations*(totalStations+1) // 2))]
    
    
    stations = [[] for i in range(totalStations+1)]
    
    
    
    if totalBuslines > totalStations*(totalStations - 1) // 2:
        
        return -1
    
    elif totalBuslines < totalStations - 1:
    
        return -1
    
    else:
        
        for i in range(totalStations-1):
            
             stations[i].append(i+1)
            
             distinctHash[i+1 + i] = True
             
             totalBuslines -= 1
            
        
        for i in range(totalStations):

            for j in range(i+1,totalStations):

                if totalBuslines == 0:

                    return stations

                if distinctHash[i+j] == False and i != j:

                    distinctHash[i+j] = True
                    totalBuslines -= 1
                    stations[i].append(j)


        if totalBuslines > 0:

            return -1
                    
                       

result = buslines()

if result == -1:

    print(-1)

else:

    for i in range(len(result)):

        for item in result[i]:

            print(str(i+1) + ' ' + str(item+1))
