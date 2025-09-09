import sys

dataInput = []
letterDict = {}
final = []


for line in sys.stdin:
    data = str(line)
    dataInput.append(data)

for character in dataInput[0]:
    
    letterDict[character] = True

memoArray = dataInput[1].split()

for word in memoArray:
    
    wordCount = len(word)
    flag = False
    
    for character in word: 
        
        if letterDict.get(character) == True:
        
            final.append('*'*wordCount)
            flag = True
            break
    
    if flag == False:
        
        final.append(word)
   
print(' '.join(final))