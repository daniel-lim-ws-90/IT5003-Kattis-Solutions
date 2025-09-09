from collections import deque

stack = deque()

N = int(input())
inputString = str(input())
inputArray = inputString.split()
operationString = str(input())
refDict = {}

refDict['A'] = 0
refDict['B'] = 1
refDict['C'] = 2
refDict['D'] = 3
refDict['E'] = 4
refDict['F'] = 5
refDict['G'] = 6
refDict['H'] = 7
refDict['I'] = 8
refDict['J'] = 9
refDict['K'] = 10
refDict['L'] = 11
refDict['M'] = 12
refDict['N'] = 13
refDict['O'] = 14
refDict['P'] = 15
refDict['Q'] = 16
refDict['R'] = 17
refDict['S'] = 18
refDict['T'] = 19
refDict['U'] = 20
refDict['V'] = 21
refDict['W'] = 22
refDict['X'] = 23
refDict['Y'] = 24
refDict['Z'] = 25

for letter in operationString:
    
    if refDict.get(letter) != None:
        
        stack.append(inputArray[refDict[letter]])
    
    elif letter == '*':
        
        x = stack.pop()
        y = stack.pop()
        
        if x == 'T' and y == 'T':
            
            stack.append('T')
        
        else:
            
            stack.append('F')
    
    elif letter == '+':
        
        x = stack.pop()
        y = stack.pop()
        
        if x == 'T' or y == 'T':
            
            stack.append('T')
        
        else:
            
            stack.append('F')
    
    elif letter == '-':
        
        x = stack.pop()
        
        
        if x == 'T' :
            
            stack.append('F')
        
        else:
            
            stack.append('T')

final = stack.pop()

print(final)
