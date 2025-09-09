import sys

result = []
input = []
for line in sys.stdin:
    input.append(line)

wordInput = str(input[0])
wordCount = int(input[1])


for i in range(wordCount):
    
     result.append(wordInput.strip())

final = ''.join(result)

print(final)