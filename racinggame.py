import heapq
players = []

Q = int(input())

smallList = []


for i in range(Q):
    
    command = str(input())
    command = command.split()
    
    
    if command[0] == '1':
        


        #heapq.heappush(players, [int(command[1]), command[1]])


        if len(smallList) < 10:



            heapq.heappush(smallList, -int(command[1]))



        elif -int(command[1]) > smallList[0] :


             heapq.heapreplace(smallList, -int(command[1]))

            
             
    
    elif command[0] == '2':
        
        Y = int(command[1])



        for i in range(len(smallList)):

            smallList[i] -= Y
        
        #for player in players:
            
            #player[0] += Y

    
    elif command[0] == '3':

        
        n = int(command[1])

        length = len(smallList)

        x = heapq.nsmallest(length - n + 1, smallList, key=None)

        print(-x[-1])

      

    

       

        

            

       

        

        
        


        

       

        

      

            

            



            

    
    
    
    
        
        
