import heapq

parameters = str(input())
parameters = parameters.split()

V = int(parameters[0])
E = int(parameters[1])

graph = [[] for i in range(V)]

visited = [False for i in range(V)]

distance = [float('inf') for i in range(V)]

parent = [-1 for i in range(V)]

for i in range(E):
    
    bridge = str(input())
    bridge = bridge.split()
    
    s = int(bridge[0])-1
    t = int(bridge[1])-1
    
    if bridge[2] == '0':
        
        graph[s].append((1,t))
        graph[t].append((1,s))
    
    else:
        
        graph[s].append((10**7,t))
        graph[t].append((10**7,s))
        

Q = []

heapq.heappush(Q,(0,0))
parent[0] = 0
distance[0] = 0

while len(Q) > 0:
    
    elt = heapq.heappop(Q)
    visited[elt[1]] = True

    #print(elt)
    
    if elt[1] == V-1:
        
        break
    
    for point in graph[elt[1]]:
        
        if visited[point[1]] == False and distance[point[1]] > distance[elt[1]] + point[0]:
            
            distance[point[1]] = distance[elt[1]] + point[0]
            heapq.heappush(Q, (distance[point[1]], point[1]))
            parent[point[1]] = elt[1]
            
        
minD = distance[V-1] % (10**7)
totalDistance = distance[V-1] - minD
totalDistance = totalDistance // (10**7)




print(totalDistance)
