start = str(input())
num = int(input())

animalDict = {}

for i in range(num):
    
    animal = str(input())
    
    if animalDict.get(animal[0]) == None:
        
        animalDict[animal[0]] = [animal]
    
    else:
        
        animalDict[animal[0]].append(animal)



if animalDict.get(start[-1]) == None:
    
    print('?')

else:
    
    flag = False

    x = animalDict[start[-1]][0]


    if x[0] == x[-1] and len(animalDict[start[-1]]) == 1:

    
        flag = True
        print(animalDict[start[-1]][0] + '!')


    else:

    
        for elt in animalDict[start[-1]]:

        
            if animalDict.get(elt[-1]) == None:
            
                print(elt + '!')
                flag = True
                break
    

    if flag == False:
        
        print(animalDict[start[-1]][0])
        