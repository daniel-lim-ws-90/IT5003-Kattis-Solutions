from collections import deque 

def dfsI(graph, start, visited):
    
    stackArray = deque()
    
    if visited[start] == True:
        
        return
    
    stackArray.append(start)
    visited[start] = True
    
    while len(stackArray) > 0:
        
        elt = stackArray.pop()
        
        
        for point in graph[elt]:
            
            if visited[point] == False:
                
                visited[point] = True
                stackArray.append(point)
                
                


parameters = str(input())
parameters = parameters.split()

N = int(parameters[0])
M = int(parameters[1])

graph = [[] for i in range(N)]
visited = [False for i in range(N)]

for i in range(M):
    
    edge = str(input())
    edge = edge.split()
    
    v1 = int(edge[0]) - 1
    v2 = int(edge[1]) - 1
    
    graph[v1].append(v2)
    graph[v2].append(v1)

count = 0 

for i in range(N):
    
    if visited[i] == False:
        
         dfsI(graph, i, visited)
         count += 1

if count == 1:
    
    print('YES')

else:
    
    print('NO')
        
        
    
    