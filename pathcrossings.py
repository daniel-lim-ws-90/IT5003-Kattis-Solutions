import math

variables = str(input())
variables = variables.split()
N = int(variables[0])
Plength = int(variables[1])
pingArray = []

def euclidenDistance(P,Q):
    
    return math.sqrt((P[0] - Q[0])**2 + (P[1] - Q[1])**2)

for i in range(Plength):
    x = str(input())
    x = x.split()
    pingArray.append((int(x[0]),int(x[1]),int(x[2]),int(x[3])))

pingArray = sorted(pingArray,key = lambda x : x[3])



answer = []

for i in range(Plength-1):
    
    Q = [pingArray[i][1],pingArray[i][2]]
    
    for j in range(i+1,Plength):
        
        U =  [pingArray[j][1],pingArray[j][2]]

        if abs(pingArray[j][3] - pingArray[i][3]) > 10:
            
            break
            
        elif abs(pingArray[j][3] - pingArray[i][3]) <= 10 and euclidenDistance(U,Q) <= 1000 and pingArray[j][0] != pingArray[i][0]:
            
            answer.append((pingArray[i][0],pingArray[j][0]))
        
        

#print(len(answer))
#answer = sorted(answer, key=lambda ans: (ans[0],ans[1]))

new_players = list(set([tuple(sorted(player)) for player in answer]))
new_players = sorted(new_players, key = lambda x: (x[0], x[1]))


if len(new_players) > 0:
    print(len(new_players))

    for i in range(len(new_players)):
        print(*new_players[i])

else:
    print(int(0))
