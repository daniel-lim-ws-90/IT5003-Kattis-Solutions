n = int(input())

countryDict = {}

for i in range(n):
    
    country = str(input())
    
    country = country.split()
    
    if countryDict.get(country[0]) == None:
        
        countryDict[country[0]] = [int(country[1])]
    
    else:
        
        countryDict[country[0]].append(int(country[1]))

for key in countryDict.keys():
    
    countryDict[key].sort()


k = int(input())

for i in range(k):
    
    country = str(input())
    country = country.split()
    
    index = int(country[1]) - 1
    
    print(countryDict[country[0]][index])
    
    
        
        