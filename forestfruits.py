import heapq
from collections import deque 

parameters = str(input())
parameters = parameters.split()

V = int(parameters[0])
E = int(parameters[1])
C = int(parameters[2])
K = int(parameters[3])
M = int(parameters[4])

graph = [[] for i in range(V)]

for i in range(E):

    edge = str(input())
    edge = edge.split()
    v1 = int(edge[0])-1
    v2 = int(edge[1])-1
    w = int(edge[2])
    graph[v1].append((w,v2))
    graph[v2].append((w,v1))

fruitPatch = str(input())
fruitPatch = fruitPatch.split()

parent = [0 for i in range(V)]
visited = [False for i in range(V)]
distance = [float('inf') for i in range(V)]
inPatch = [False for i in range(V)]

for elt in fruitPatch:

    i = int(elt) - 1
    inPatch[i] = True




def shortestPath(start, end, graph, visited, parent, distance):

    pq = []

    heapq.heappush(pq, (0, start))
    distance[start] = 0
    count = 0

    #visited = [False for i in range(V)]

    while len(pq) > 0:

        
        elt = heapq.heappop(pq)

        if elt == end:

            return

        #if elt[0] > distance[elt[1]]:

            #continue

        
        visited[elt[1]] = True

      


        for point in graph[elt[1]]:
               
                if visited[point[1]] == False and  distance[point[1]] > distance[elt[1]] + point[0]:
                   
                    distance[point[1]] = distance[elt[1]] + point[0]
                    heapq.heappush(pq, (distance[point[1]], point[1]))
                    parent[point[1]] = elt[1]
                    


for i in range(V):

    if inPatch[i] == True and visited[i] == False:

        shortestPath(0,i,graph,visited, parent, distance)

#print(distance)

grow = deque()
consume = []

for number in fruitPatch:

    i = int(number)-1

    if distance[i] < 100000000000000:
    
        consume.append(distance[i])


#print(consume)

consume.sort()
maxDist = 0
consume = deque(consume)

while M >= 2*K:

    M -= K




while len(consume) > 0:

    if M == 0:
        break

    x = consume.popleft()
    #print(2*x)
    grow.append(x)
    M -= 1

    if x > maxDist:

        maxDist = x

    if len(grow) == K:

        y = grow.popleft()
        consume.appendleft(y)

#print(C)
if M > 0 and len(consume) == 0:

    print(-1)

elif M == 0 and len(consume) >= 0:

    print(2*maxDist)
        
    


    

    




    






    






