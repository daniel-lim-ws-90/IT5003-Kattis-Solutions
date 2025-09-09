parameters = str(input())
parameters = parameters.split()

N = int(parameters[0])
M = int(parameters[1])

friendDict = {}

for i in range(N):

    friendDict[str(i+1)] = []

for i in range(M):
    
    x = str(input())
    
    x= x.split()

        
    friendDict[x[0]].append( int(x[1]))

    friendDict[x[1]].append( int(x[0]))


final = []

for elt in friendDict.keys():
    
    x = int(elt)
    
    y = len(friendDict[elt]) - x

    z = str(y)
    
    final.append(z)

print(' '.join(final))