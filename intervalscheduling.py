N = int(input())
points = []

for i in range(N):
    
    x = str(input())
    arr = x.split()
    points.append((int(arr[0]),int(arr[1])))
    

points = sorted(points, key=lambda coord: coord[1])

count = 1
end = points[0][1]

for i in range(1,N):
    
    if points[i][0] >= end:
        
        count += 1
        end = points[i][1]

print(count)
    
    