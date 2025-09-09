def binary_search(arr, x):
    
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid][2] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid][2] > x:
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return low

N = int(input())

coordinates = []

for i in range(N):
    
    stringInput = str(input())
    stringSplit = stringInput.split()
    x = int(stringSplit[0])
    y = int(stringSplit[1])
    distance = x**2 + y**2
    coordinates.append((x,y,distance))
    
Q = int(input())

power = []
result = []

for i in range(Q):
    
    power.append(int(input()))
    
coordinates.sort(key=lambda a: a[2])

for elt in power:
    
    
    count = binary_search(coordinates, elt**2)

    result.append(count)

for elt in result:
    
    print(elt)
    