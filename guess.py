high = 1000
low = 1
mid = (high+low) // 2
print(mid)

while (True):
    
    result = input()
    if result == 'higher':
        
        low = mid +1
        mid = (high + low) // 2
        print(mid)
        
        
    elif result == 'lower':
        
        high = mid -1 
        mid = (high + low) // 2
        print(mid)
    
    elif result == 'correct':
        break
    