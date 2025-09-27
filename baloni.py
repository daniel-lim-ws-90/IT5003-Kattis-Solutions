N = int(input())
array = str(input())
array = array.split()

count = 0  
arrowSet = {}
entries = []

for i in range(N):
    
    entry = int(array[i])
    entries.append(entry)

    if arrowSet.get(str(entry)) == None:

        arrowSet[str(entry)] = 0




for entry in entries:

    if arrowSet.get(str(entry)) == 0:

        count += 1
        
        if entry > 1 and arrowSet.get(str(entry-1)) != None:

           arrowSet[str(entry-1)] += 1

    else:

       arrowSet[str(entry)] -= 1

       if entry > 1 and arrowSet.get(str(entry-1)) != None:

           arrowSet[str(entry-1)] += 1

    



print(count)
