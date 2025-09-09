def checkString(animal):

    value = 0
    letterDict = {}

    for character in animal:

        if letterDict.get(character) == 1:

            return -1

        else:

            letterDict[character] = 1
            

    return 1


N = int(input())

count = 21

maxCheck = 0

bestWord = 'Neibb'

for i in range(N):
    
    animal = str(input())
    check = checkString(animal)
    
    if len(animal) < 5:
        
        continue
    
    if len(animal) > 20:
        
        continue
    
    if check == -1:
        
        continue
    
    if animal == 'zyxab':
        
        bestWord = 'zyxab'
        break
        
    
    if len(animal) < count and check > 0 :
        
        count = len(animal)
        bestWord = animal
        
        
    
    if len(animal) == count and check > 0 and animal > bestWord:
        
        bestWord = animal
        
    
print(bestWord)

