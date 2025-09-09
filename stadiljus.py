N = int(input())
x = int(input())
y = int(input())
values = str(input())
placeArray = values.split()
numArray = []

for elt in placeArray:
    
    numArray.append(int(elt))


numArray.sort()


total = 0
count = 0

for i in range(N):
    
    total += numArray[i]*x
    
    if total/(i+1) > y:
        
        count = i
        
        break
    
    
    else:
        
        count += 1

print(count)