import sys

test = int(input())

for i in range(test):

    parameters = str(input())
    parameters = parameters.split()

    cols = int(parameters[0])
    rows = int(parameters[1])
    record = []

    for i in range(rows):

        row = str(input())
        row = row.split()

        for j in range(cols):

            weight = int(row[j])

            if weight > 0:
                
                record.append((i,j,weight))

    total = sys.maxsize

    i = 0
    j = 0

    total = 0

    for elt in record:

            x = abs(0 - elt[0])
            y = abs(0 - elt[1])
            weight = elt[2]

            total += (x + y)*weight

    
    while i < rows - 1 and j < cols - 1:

            distance = [0,0]
           

            for elt in record:

                x = abs(i + 1 - elt[0])
                y = abs(j - elt[1])
                weight = elt[2]

                distance[0] += (x + y)*weight

            for elt in record:

                x = abs(i - elt[0])
                y = abs(j + 1 - elt[1])
                weight = elt[2]

                distance[1] += (x + y)*weight



            index = 0
            minVal = distance[0]

            for k in range(1,2):
                
                if distance[k] < minVal:

                    minVal = distance[k]
                    index = k

            if minVal < total:

                total = minVal

                if index == 0:

                    i += 1

                if index == 1:

                    j += 1


            else:

                break
                

            

    print(str(total) + ' blocks')
