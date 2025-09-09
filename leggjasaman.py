import sys
x = 0
for line in sys.stdin:
    data = int(line)
    x += data
print(x)