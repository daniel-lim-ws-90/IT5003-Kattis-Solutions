n = int(input())

adj1 = []

#adj2 = []

zeros = [[0]*n]*n

for i in range(n):
    
    row = str(input())
    row = row.split()
    numrow = []
    for elt in row:
        numrow.append(int(elt))
    
    adj1.append(numrow)
    #adj2.append(numrow)



result = [] # final result
for i in range(len(adj1)):

    row = [] # the new row in new matrix
    for j in range(i,len(adj1[0])):
        
        product = 0 # the new element in the new row
        for v in range(len(adj1[i])):
            product += adj1[i][v] * adj1[v][j]
           
        row.append(product) # append sum of product into the new row
        
    result.append(row) # append the new row into the final result




for row in result:

    while len(row) < n:

        row.insert(0,-1)

for i in range(n):

    for j in range(n):

        if result[i][j] == -1:

            result[i][j] = result[j][i]


traceArray = []


for i in range(n):

    summation = 0

    for j in range(n):

        summation += adj1[i][j] * result[j][i]

    traceArray.append(summation)

        

trace = 0

for i in range(n):

    trace += traceArray[i]

trace = trace //6

print(trace)




