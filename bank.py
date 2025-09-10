import heapq

firstHeap = []

Parameters = str(input())
Parameters = Parameters.split()

N = int(Parameters[0])
T = int(Parameters[1])

for i in range(N):
    
    entry = str(input())
    entry = entry.split()
    
    deposit = int(entry[0])
    time = int(entry[1])

    firstHeap.append((-deposit, time))
    
heapq.heapify(firstHeap)

taken = 0
total = 0

timeSlot = [[] for i in range(T+1)]

while taken <= T+1 and len(firstHeap) > 0:

    item = heapq.heappop(firstHeap)
    time = item[1]

    for i in range(time+1):

        if len(timeSlot[time-i]) == 0:

            timeSlot[time-i].append(item)
            taken += 1
            break
    
#print(timeSlot)
           

for elt in timeSlot:

    if len(elt) > 0:

         total += elt[0][0]

         

print(-total)
