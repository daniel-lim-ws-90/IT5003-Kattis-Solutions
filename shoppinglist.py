parameters = str(input())
parameters = parameters.split()

N = int(parameters[0])

itemSet = set()

shoppingList = str(input())
shoppingList = shoppingList.split()

for item in shoppingList:
    
    itemSet.add(item)

for i in range(N-1):

    newItemSet = set()
    shoppingList = str(input())
    shoppingList = shoppingList.split()

    for item in shoppingList:
    
        newItemSet.add(item)

    itemSet = newItemSet & itemSet
    

itemSet = sorted(itemSet)

print(len(itemSet))

for item in itemSet:

    print(item)