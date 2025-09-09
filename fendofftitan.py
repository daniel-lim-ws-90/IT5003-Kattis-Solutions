import heapq
 

iPair = tuple
 

class Graph:
    
    def __init__(self, V: int): # Constructor
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.parent = [-1 for i in range(V)]
        self.adj2 = [[] for _ in range(V)]
        
 
    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))
    
    def addEdge2(self, u: int, v: int, w: int):
        self.adj2[u].append((v, w))
        self.adj2[v].append((u, w))
 
   
    def shortestPath(self, src: int, end: int, result):
      
        pq = []
        heapq.heappush(pq, (0, src))
        
        
 
        dist = [float('inf')] * self.V
        dist[src] = 0
        self.parent[src] = src
 
        while pq:
         
            d, u = heapq.heappop(pq)

            if u == end:

                break
 
            
            for v, weight in self.adj[u]:
               
                if dist[v] > dist[u] + weight:
                   
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))
                    self.parent[v] = u
 
     

        start = end

        if dist[end] == float('inf'):

            return -1


        count = 0
        while (True):

            if start == src:


                break

            for i in range(len(self.adj[start])):

                if self.adj[start][i][0] == self.parent[start]:

                    count += self.adj2[start][i][1]


                    if self.adj[start][i][1] > (M*1000000000)**9 :
    
                        result[2] += 1

                    elif self.adj[start][i][1] > (M*1000000000)**3:

                        result[1] += 1

            start = self.parent[start]

        return count


        

            
        
 

if __name__ == "__main__":
    

    result = [0,0,0]
    parameters = str(input())
    parameters = parameters.split()
    
    flag1 = False
    flag2 = False
   

    N = int(parameters[0])
    M = int(parameters[1])
    X = int(parameters[2])
    Y = int(parameters[3])

    g = Graph(N)
    


    for i in range(M):

        path = str(input())
        path = path.split()

        a = int(path[0])
        b = int(path[1])
        w = int(path[2])
        c = int(path[3])


        if c == 0:

            g.addEdge(a-1, b-1, w)
            g.addEdge2(a-1, b-1,  w  )
            

        if c == 1:
            
            flag1 = True

            g.addEdge(a-1, b-1,  w + (M*1000000000)**3 )
            g.addEdge2(a-1, b-1,  w  )
            

        if c == 2:
            
            flag2 = True

            g.addEdge(a-1, b-1,  w + (M*1000000000)**9 )
            g.addEdge2(a-1, b-1,  w  )
            

 
    flag = g.shortestPath(X-1, Y-1, result)

    stringResult = []

    if flag > -1:

        result[0] = flag

 
        

    for x in result:

        stringResult.append(str(x))

    
    if flag > -1:

        
        print(' '.join(stringResult))

    else:

        print('IMPOSSIBLE')

    
