from collections import deque
import heapq

parameters1 = str(input())
parameters2 = str(input())

parameters1 = parameters1.split()
parameters2 = parameters2.split()

N = int(parameters1[0])
D = int(parameters1[1])
C = int(parameters2[0])
infectedIndex = {}
visited = [False for i in range(N)]
contactList = [[] for i in range(N)]


for i in range(1,C+1):

    num = int(parameters2[i])-1
    infectedIndex[str(num)] = 1
    visited[num] = True



edgeList = []
infectedQ = deque()
enterRoom = []
exitRoom = []
group = set()



for i in range(N):
    
    edge = str(input())
    edge = edge.split()
    edgeList.append((int(edge[0]), int(edge[1]), i))

    heapq.heappush(enterRoom, (int(edge[0]),i))

    heapq.heappush(exitRoom, (int(edge[1]),i))

    if infectedIndex.get(str(i)) == 1:

        infectedQ.append(i)



while len(enterRoom) > 0:


    item = enterRoom[0]
  
    if item[0] > exitRoom[0][0]:

        noContact = heapq.heappop(exitRoom)
        group.remove(noContact[1])

    else:


        for elt in group:

            contactList[elt].append(item[1])
            contactList[item[1]].append(elt)

            
        group.add(item[1])
        heapq.heappop(enterRoom)

        

        


for j in range(D):

    
    Q = len(infectedQ)



    for i in range(Q):
        
        index = infectedQ.popleft()

        visited[index] = True

        for elt in contactList[index]:

                if visited[elt] == False:

                    infectedQ.append(elt)
                    #infected D+1 day
                    visited[elt] = True

      
    
persons = []


for j in range(len(visited)):

    if visited[j] == True:

        persons.append(str(j+1))

print(' '.join(persons))









       
            

                
                

                

    
    








    

    
