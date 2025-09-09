N = int(input())

numDict = {}

for i in range(N):

    num = int(input())

    if numDict.get(num) != None:

        numDict[num] += 1

        ans = num*(numDict[num])

        while numDict.get(ans) != None:

            numDict[num] += 1

            ans = num*(numDict[num])

        numDict[ans] = 1

    else:

        numDict[num] = 1

            

                   

for key in numDict.keys():

    print(key)