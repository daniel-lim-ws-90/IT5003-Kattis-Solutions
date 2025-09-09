x = float(input())
y = (x*5280/4854)*1000
z = int(y)
remainder = y - z
if remainder >= 0.5:
    print(z+1)
else:
    print(z)