totalStudent = int(input())
studentDict = {}

for i in range(totalStudent):

    name = str(input())
    studentDict[name] = 0

totalClass = int(input())

for i in range(totalClass):

    inputString = str(input())
    inputString = inputString.split()

    

    students = int(inputString[0])

    for j in range(students):

        name = inputString[1+j]

        if studentDict.get(name) != None:

            studentDict[name] += 1


sorted_studentDict = sorted(studentDict.items(), key=lambda kv: kv[1], reverse=True)

for item in sorted_studentDict:

    output = str(item[1]) + " " + item[0]
    print(output)