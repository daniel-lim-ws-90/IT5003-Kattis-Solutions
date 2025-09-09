N = int(input())
M = N // 3

S = str(input())

stringArray = S.split()

numArray = []

for item in stringArray:
    
    numArray.append(int(item))

numArray.sort()

resultArray =  numArray[M:2*M] + numArray[:M] + numArray[2*M:3*M] 

for item in resultArray:

    print(str(item), end=' ')