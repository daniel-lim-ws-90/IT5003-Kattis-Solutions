from collections import deque

def bfsDistance(graph, start, visited, N, M):
    
    qArray = deque()
    
    if visited[start[0]][start[1]] == True:
        
        return 0
    
    qArray.append(start)
    visited[start[0]][start[1]] = True
    #count = -1
    
    while (len(qArray)) > 0:
        
        elt = qArray.popleft()
        #count += 1
        #print(elt)
        #print(visited)

        if elt[0] == 0:

            return elt[2]

        if elt[1] == 0:

            return elt[2]
        
        if elt[0] == N - 1:
            
            return elt[2]
        
        if elt[1] == M - 1:
            
            return elt[2]
        
        if (graph[elt[0]-1][elt[1]] == '0' or graph[elt[0]-1][elt[1]] == 'D') and visited[elt[0]-1][elt[1]] == False:

            #print('UP')
            qArray.append((elt[0]-1,elt[1], elt[2]+1))
            visited[elt[0]-1][elt[1]] = True
        
        if (graph[elt[0]+1][elt[1]] == '0' or graph[elt[0]+1][elt[1]] == 'U') and visited[elt[0]+1][elt[1]] == False:

            #print('DOWN')
            qArray.append((elt[0]+1, elt[1], elt[2]+1))
            visited[elt[0]+1][elt[1]] = True
        
        if (graph[elt[0]][elt[1]-1] == '0' or graph[elt[0]][elt[1]-1] == 'R') and visited[elt[0]][elt[1]-1] == False:
            
            #print('LEFT')
            qArray.append((elt[0], elt[1]-1, elt[2]+1))
            visited[elt[0]][elt[1]-1] = True
            
        
        if (graph[elt[0]][elt[1]+1] == '0' or graph[elt[0]][elt[1]+1] == 'L') and visited[elt[0]][elt[1]+1] == False:
            #print('RIGHT')
            qArray.append((elt[0], elt[1]+1, elt[2]+1))
            visited[elt[0]][elt[1]+1] = True
    
    
    return 'NOT POSSIBLE'
            
            


parameters = str(input())
parameters = parameters.split()

t = int(parameters[0])
N = int(parameters[1])
M = int(parameters[2])

grid = []

visited = []

for i in range(N):

    row = []

    for j in range(M):

        row.append(False)

    visited.append(row)


start = (0,0,0)

for i in range(N):
    
    row = str(input())
    grid.append(row)
    
    for j in range(M):
        
        if row[j] == 'S':
            
            start = (i,j,0)

#visited[start[0]][start[1]] = True
#print(visited)
final = bfsDistance(grid, start, visited, N, M)

if final == 'NOT POSSIBLE':

    print('NOT POSSIBLE')

elif final <= t:

    print(final)

else:

    print('NOT POSSIBLE')


