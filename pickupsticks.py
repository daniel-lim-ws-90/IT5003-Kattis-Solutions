from collections import deque

parameters = str(input())
parameters = parameters.split()

n = int(parameters[0])
m = int(parameters[1])

adj = [[] for i in range(n)]

for i in range(m):
    
    entry = str(input())
    entry = entry.split()
    a = int(entry[0]) - 1
    b = int(entry[1]) - 1
    
    adj[a].append(b)
    

def topologicalSort(n,adj):
    
    indegree = [0] * n

    # Calculate indegree of each vertex
    for u in range(n):
        for v in adj[u]:
            indegree[v] += 1

    #print(indegree)

    # Queue to store vertices with indegree 0
    q = deque([i for i in range(n) if indegree[i] == 0])
    
    result = []
    
    while q:
        node = q.popleft()
        result.append(node)

        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    # Check for cycle
    if len(result) != n:
        #print(result)
        print("IMPOSSIBLE")
        return
    else:
        for x in result:
            print(x+1)

topologicalSort(n,adj)  
