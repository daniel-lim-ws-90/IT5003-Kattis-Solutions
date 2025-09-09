import sys

kcount = 0
bcount = 0
 
for line in sys.stdin:
    data = str(line)
    
    for letter in data:
        
        if letter == 'k':
            
            kcount += 1
        
        elif letter == 'b':
            
            bcount += 1

if kcount == 0 and bcount == 0:
    
    print('none')

elif kcount == bcount:
    
    print('boki')

elif kcount > bcount:
    
    print('kiki')

else:
    
    print('boba')