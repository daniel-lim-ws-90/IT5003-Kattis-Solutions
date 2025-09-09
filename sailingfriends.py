def dfsIterative(start,graph,visited):
    
    stackArray = []
    
    if visited[start] == True:
        
        return
    
    else:
        
        stackArray.append(start)
        
        while len(stackArray) > 0:
            
            elt = stackArray.pop()
            visited[elt] = True
            for point in graph[elt]:

                if visited[point] == False:
                
                    stackArray.append(point)
                    visited[point] = True
            


def dfs(start,graph,visited):
    
    
    if visited[start] == True:
        
        return
    
    else:
        
        visited[start] = True
        
        
        for point in graph[start]:
            
            dfs(point,graph,visited)
            
            

parameters = str(input())
parameters = parameters.split()

N = int(parameters[0])
B = int(parameters[1])
M = int(parameters[2])

boatpeople = str(input())
boatpeople = boatpeople.split()



graphDict = {}
visitedDict = {}
count = 0

for i in range(N):
    
    graphDict[str(i+1)] = []
    visitedDict[str(i+1)] = False

for i in range(M):
    
    pair = str(input())
    pair = pair.split()
    
    graphDict[pair[0]].append(pair[1])
    graphDict[pair[1]].append(pair[0])

for boat in boatpeople:
    
    dfsIterative(boat,graphDict,visitedDict)
    
for key in visitedDict.keys():
    
    if visitedDict[key] == False:
        
        dfsIterative(key,graphDict,visitedDict)
        count += 1

print(count)
        
        


    
    



