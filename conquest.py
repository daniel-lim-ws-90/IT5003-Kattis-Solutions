from collections import deque
import heapq


def addEdgeUndirected(adj, u, v):
 
    adj[u].append(v)
    adj[v].append(u)


def bfs1(start, graph,visited, battlePower, N):

    sortArray = deque()

    maxPower = 0

    reachable = []

    sortArray.append(start)

    visited[start] = True

    maxPower = battlePower[0]

    

    while (len(sortArray)>0):


        elt = sortArray.popleft()



        for point in graph[elt]:

            if visited[point] == False and battlePower[point] < maxPower:

                sortArray.append(point)
                maxPower += abs(battlePower[point])
                visited[point] = True


            elif visited[point] == False:

                reachable.append(point)
                visited[point] = True


        for point in reachable:

            if battlePower[point] < maxPower:

                sortArray.append(point)
                maxPower += abs(battlePower[point])
                reachable.remove(point)
                
                        
                
    return maxPower 





parameters = str(input())
parameters = parameters.split()

N = int(parameters[0])
M = int(parameters[1])

graph = [[] for i in range(N)]
battlePower = []
visited =  [False for i in range(N)]


for i in range(M):

    edge = str(input())
    edge = edge.split()
    addEdgeUndirected(graph, int(edge[0])-1, int(edge[1])-1)

for i in range(N):

    powerLevel = int(input())
    battlePower.append(powerLevel)

visited[0] = True


maxPower = bfs1(0, graph,visited, battlePower, N)

print(maxPower)
