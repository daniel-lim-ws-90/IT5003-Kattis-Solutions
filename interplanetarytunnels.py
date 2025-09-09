
from collections import deque

def addEdgeUndirected(adj, u, v):
 
    adj[u].append(v)
    adj[v].append(u)
    
 

def bfs(bobStart, aliceStart, graph,visitedBob):

   

    if bobStart == aliceStart:

        return 0
    
    
    stackArrayBob = deque()
   
        
    stackArrayBob.append(bobStart)
    


    visitedBob[bobStart] = 0
    
        
    while (len(stackArrayBob) > 0):
   
        

        elt1 = stackArrayBob.popleft()

    

        if elt1 == aliceStart:

            return visitedBob[elt1]


        for point in graph[elt1]:

        

            if visitedBob[point] == -1:
                    
                stackArrayBob.append(point)
                visitedBob[point] = visitedBob[elt1] + 1
                    

            if point == aliceStart:

                 return visitedBob[point]

            
           



parameter1 = str(input())
parameter1 = parameter1.split()

N = int(parameter1[0])
M = int(parameter1[1])

parameter2 = str(input())
parameter2 = parameter2.split()

aliceStart = int(parameter2[0])
bobStart = int(parameter2[1])



graph = [[] for i in range(N)]

visitedBob = [-1 for i in range(N)]
visitedAlice = [-1 for i in range(N)]


for i in range(M):

    pair = str(input())

    pair = pair.split()
    
   
    addEdgeUndirected(graph, int(pair[0]), int(pair[1]))
        

result = bfs(bobStart, aliceStart, graph,visitedBob)

if result%2 == 0:

    print(result//2)

else:

    print(result//2+1)







