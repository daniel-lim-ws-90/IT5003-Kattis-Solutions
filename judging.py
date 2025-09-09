N = int(input())
kattis = {}
dom = {}
for i in range(N):
    
    x = str(input())
    if kattis.get(x) == None:
        
        kattis[x] = 1
    else:
        
        kattis[x] += 1

for i in range(N):
    
    x = str(input())
    if dom.get(x) == None:
        
        dom[x] = 1
    else:
        
        dom[x] += 1

allkeys = {}

for key in kattis.keys():
    
    allkeys[key] = True

for key in dom.keys():
    
    if  allkeys.get(key) == None:
        
        allkeys[key] = True

count = 0

for x in allkeys.keys():
    
    if dom.get(x) != None and kattis.get(x) != None:
        
        count += min(kattis[x],dom[x])


print(count)