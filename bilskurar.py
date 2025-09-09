def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid][2] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid][2] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return low
    
def merge(arr, l, m, r):

    count = 0
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    

    for elt in L:

        threshold = elt[2]
        result = binary_search(R, 0, len(R)-1, threshold)
        count += result

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i][2] <= R[j][2]:
            arr[k] = L[i]
            i += 1
            
        else:
            arr[k] = R[j]
            j += 1
            
            
        k += 1
    
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        

    # l is for left index and r is right index of the
    # sub-array of arr to be sorted

   

    if count > 0:

        return count
    

    else:

        return 0

def mergeSort(arr, l, r):
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2

        # Sort first and second halves
        return mergeSort(arr, l, m) + mergeSort(arr, m+1, r) + merge(arr, l, m, r)
        

    else:

        return 0



N = int(input())
P = str(input())
Q = str(input())


strArray1 = P.split()
strArray2 = Q.split()

array1 = []
array2 = []

for elt in strArray1:
    
    array1.append(int(elt))

for elt in strArray2:
    
    array2.append(int(elt))


secondArrayDict = {}


for i in range(N):
    
    key = str(array2[i])
    secondArrayDict[key] = i

array3 = []

for i in range(N):
    
    compareKey = compareKey = str(array1[i])
    thirdElt = secondArrayDict.get(compareKey)
    array3.append((array1[i],i,thirdElt))


count = mergeSort(array3, 0, N-1)


    
print(count)

    

    
