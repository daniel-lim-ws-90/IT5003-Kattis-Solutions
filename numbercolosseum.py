from queue import LifoQueue

N = int(input())
positiveQ = []
negativeQ = []


stringArray = str(input())
stringArray = stringArray.split()

positiveTotal = 0
negativeTotal = 0


for i in range(N):

    
        
    if int(stringArray[i]) < 0 and len(positiveQ) == 0:
        
        negativeQ.append(int(stringArray[i]))
        negativeTotal += int(stringArray[i])
        
    
    elif int(stringArray[i]) > 0 and len(negativeQ) == 0:
        
        positiveQ.append(int(stringArray[i]))
        positiveTotal += int(stringArray[i])


    elif int(stringArray[i]) < 0 and len(positiveQ) > 0:

        y = int(stringArray[i])

        if abs(y) > abs(positiveTotal):

            y += positiveTotal
            positiveTotal = 0
            positiveQ = []
            negativeQ.append(y)
            negativeTotal += y

        elif abs(y) == abs(positiveTotal):

            y = 0
            positiveTotal = 0
            positiveQ = []
            
            
            
        else:
            
            while len(positiveQ) > 0 and y < 0:

                x = positiveQ[-1]
                w = y + x
                #print(w)
                #positiveTotal -= x

                if w > 0:

                    positiveQ[-1] = w
                    positiveTotal += w - x
                    y = 0
                    break

                elif w < 0:

                    y = w
                    positiveQ.pop()
                    positiveTotal -= x

                elif w == 0:
                    
                    y = 0
                    positiveQ.pop()
                    positiveTotal -= x
                    break

            if y < 0 and len(positiveQ) == 0:


                negativeQ.append(y)
                negativeTotal +=y

            
            
    elif int(stringArray[i]) > 0 and len(negativeQ) > 0:

        y = int(stringArray[i])

        if abs(y) > abs(negativeTotal):

            y +=negativeTotal
            negativeTotal = 0
            negativeQ = []
            positiveQ.append(y)
            positiveTotal += y

        elif abs(y) == abs(negativeTotal):

            y = 0
            negativeTotal = 0
            negativeQ = []
            
        else:
            
            while len(negativeQ)> 0 and y > 0:

                x = negativeQ[-1]
                w = x + y
                #print(w)
                #negativeTotal -= x

                if w < 0:

                    negativeQ[-1] = w
                    y = 0
                    negativeTotal += w-x
                    break

                elif w > 0:

                    y = w
                    negativeQ.pop()
                    negativeTotal -= x

                elif w == 0:
                    
                    y = 0
                    negativeQ.pop()
                    negativeTotal -= x
                    break

            if y > 0 and len(negativeQ) == 0:


                positiveQ.append(y)
                positiveTotal += y
       


    
    #while (negativeQ.empty() == False and positiveQ.empty() == False):

        #x = positiveQ.get()
        #y = negativeQ.get()
       


        #if abs(x) > abs(y):

            #x += y
            #print(x)
            #positiveQ.put(x)
            

        #elif abs(x) < abs(y):

            #y += x
            #print(y)
            #negativeQ.put(y)
            

           
    
if len(negativeQ) == 0 and len(positiveQ) == 0:
    
    print('Tie!')

elif len(positiveQ) > 0:
    
    print('Positives win!')
    #display = []
    #while positiveQ.empty() == False:
        #x = positiveQ.get()
        #display.insert(0,str(x).strip())
    final = [str(x).strip() for x in positiveQ]
    print(' '.join(final))
    
elif len(negativeQ) > 0:
    
    print('Negatives win!')
    #display = []
    #while negativeQ.empty() == False:
        #y = negativeQ.get()
        #display.insert(0,str(y).strip())
    final = [str(x).strip() for x in negativeQ]    
    print(' '.join(final))
