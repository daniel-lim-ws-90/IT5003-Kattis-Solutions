parameters1 = str(input())
parameters2 = str(input())

parameters1 = parameters1.split()
parameters2 = parameters2.split()

ansArray = []

n = int(parameters1[0])


def flow(start, ansArray, n, m):
    

    if ansArray[start[0]][start[1]] == '~':

        return

    ansArray[start[0]][start[1]] = '~'

    if start[0] == n-1:

        return

    i = start[0]
    j = start[1]

    nextMove = []

    if i < n - 1 and ansArray[i+1][j] == 'O' or ansArray[i+1][j] == '~' :


        return flow((i+1,j), ansArray, n, m)

    else:

        if j > 0 and ansArray[i][j-1] == 'O':

            nextMove.append((i,j-1))

        if j < m-1 and ansArray[i][j+1] == 'O':

            nextMove.append((i,j+1))

        

    if len(nextMove) == 0:

        return


    for elt in nextMove:


        flow(elt, ansArray, n, m)



for i in range(n):
    
    row = str(input())
    length = len(row)
    
    rowAns = []
    
    for j in range(length):
        

        rowAns.append(row[j])
    

    ansArray.append(rowAns)



m = len(ansArray[0])

d = ansArray



for column in parameters2:

    start = (0,int(column))

    flow(start, ansArray, n,m)




for r in range(len(d)): # rows   
    for c in range(len(d[r])): # columns
        print (d[r][c], sep="", end="")  
    print()
