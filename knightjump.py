from collections import deque

N = int(input())

array = []

for i in range(N):
    
    row = str(input())
    array.append(row)

neighbour = {}

startV = -1
startH = -1

for i in range(N):
    
    for j in range(N):
        
        neighbour[str(i) + ' ' + str(j)] = []

        if array[i][j] == 'K':

            startV = i
            startH = j

        

for i in range(N):
    
    for j in range(N):
        
        if i < N - 2 and j < N - 1 and array[i][j] != '#':
            
            if array[i+2][j+1] != '#':
            
                neighbour[str(i) + ' ' + str(j)].append(str(i+2) + ' ' + str(j+1))
                #neighbour[str(i+2) + ' ' + str(j+1)].append(str(i) + ' ' + str(j))
               
        
        if i < N - 2 and j > 0 and array[i][j] != '#':
            
            if array[i+2][j-1] != '#':
            
                neighbour[str(i) + ' ' + str(j)].append(str(i+2) + ' ' + str(j-1))
                #neighbour[str(i+2) + ' ' + str(j-1)].append(str(i) + ' ' + str(j))
                
        
        if i > 1 and j < N - 1 and array[i][j] != '#':
            
            if array[i-2][j+1] != '#':
            
                neighbour[str(i) + ' ' + str(j)].append(str(i-2) + ' ' + str(j+1))
                #neighbour[str(i-2) + ' ' + str(j+1)].append(str(i) + ' ' + str(j))
                
        
        if i > 1 and j > 0 and array[i][j] != '#':
            
            if array[i-2][j-1] != '#':
            
                neighbour[str(i) + ' ' + str(j)].append(str(i-2) + ' ' + str(j-1))
                #neighbour[str(i-2) + ' ' + str(j-1)].append(str(i) + ' ' + str(j))
                
        
        if i < N-1 and j < N-2 and array[i][j] != '#':

             if array[i+1][j+2] != '#':

                 neighbour[str(i) + ' ' + str(j)].append(str(i+1) + ' ' + str(j+2))
                 #neighbour[str(i+1) + ' ' + str(j+2)].append(str(i) + ' ' + str(j))
                 

        if i < N - 1 and j > 1 and array[i][j] != '#':
            
            if array[i+1][j-2] != '#':
            
                neighbour[str(i) + ' ' + str(j)].append(str(i+1) + ' ' + str(j-2))
                #neighbour[str(i+1) + ' ' + str(j-2)].append(str(i) + ' ' + str(j))
        

        if i > 0 and j < N - 2 and array[i][j] != '#':
            
            if array[i-1][j+2] != '#':
            
                neighbour[str(i) + ' ' + str(j)].append(str(i-1) + ' ' + str(j+2))
                #neighbour[str(i-1) + ' ' + str(j+2)].append(str(i) + ' ' + str(j))
                

        if i > 0 and j > 1 and array[i][j] != '#':
            
            if array[i-1][j-2] != '#':
            
                neighbour[str(i) + ' ' + str(j)].append(str(i-1) + ' ' + str(j-2))
                #neighbour[str(i-1) + ' ' + str(j-2)].append(str(i) + ' ' + str(j))


Q = deque()

Q.append((startV,startH,0))

visited = [[False for i in range(N)] for j in range(N)]

result = -1

while len(Q) > 0:

    item = Q.popleft()

    visited[item[0]][item[1]] = True

    if item[0] == 0 and item[1] == 0:

        result = item[2]
        break

    entry = str(item[0]) + ' ' + str(item[1])

    for reach in neighbour[entry]:

        reach = reach.split()

        coordy = int(reach[0])

        coordx = int(reach[1])

        if  visited[coordy][coordx] == False:

            Q.append((coordy, coordx, item[2]+1))

            visited[coordy][coordx] = True


print(result)

        
        

        


        
        
