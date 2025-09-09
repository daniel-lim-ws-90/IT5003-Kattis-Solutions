import math

n = int(input())
t = str(input())
s = str(input())
t = t.split()
s = s.split()

t_array = []


for i in range(n):
    
    if int(s[i]) > -1:
        
        t_array.append([int(s[i]), int(t[i])])

t_array = sorted(t_array, key = lambda x: x[0])
n = len(t_array)


supply = t_array[0][0]
demand = t_array[0][1]
computer = math.ceil(demand/supply)
max = computer

for i in range(1,n):
    
    time_difference = t_array[i][0] - t_array[i-1][0]
    supply += time_difference
    demand += t_array[i][1]
    predict = supply
    computer = 1
    
    if demand > predict and time_difference > 0:
        
        #slack = math.ceil((demand - predict)/time_difference)
        #computer += slack
        computer = math.ceil(demand/supply)
        
    elif demand > predict and time_difference == 0:
        
        computer = math.ceil(demand/supply)
        
    if computer > max:
        
        max = computer

print(max)
    