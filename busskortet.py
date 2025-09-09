import sys

def recursion(n, depth):
    
    if n == 500:
        return depth+1 
    elif n == 200:
        return depth+1
    elif n == 100:
        return depth+1
    elif n < 0:
        return depth
    elif n > 500:
        return recursion(n-500, depth+1)
    elif n > 400:
        return recursion(n-500, depth+1)
    elif n > 300:
        return recursion(n-200, depth+1)
    elif n > 200:
        return recursion(n-200, depth+1)
    elif n > 100:
        return recursion(n-200, depth+1)
    elif n > 0:    
        return recursion(n-100, depth+1)
        
 
for line in sys.stdin:
    data = int(line)
    print(recursion(data, 0))
