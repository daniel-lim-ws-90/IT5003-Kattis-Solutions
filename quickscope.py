

class Node:

    def __init__(self, height, parent):

        
        self.data = {} 
        self.height = height
        self.parent = parent
     
        

    def getData(self, key):

        return self.data.get(key)

    def addData(self, key, val):

        self.data[key]= val
      
    def getHeight(self):

        return self.height

   
    def getParent(self):

        return self.parent

    def getDataList(self):

        return self.data




def quickScope():

    N = int(input())
  

    start = Node(0,None)
    current = start
    
    varList = {}
    
    

    for i in range(N):
        
        elt = str(input())
        elt = elt.split()
        
        if elt[0] == '{':
            
            height = current.getHeight()+ 1
            newNode = Node(height,current)
            current = newNode

        
        elif elt[0] == '}':

            temp = current
            
            current = current.getParent()

            dataList = temp.getDataList()

            for key in dataList.keys():

                varList[key].pop()

            

            del temp
        

        elif elt[0] == 'DECLARE':
            
            key = elt[1]

            val = elt[2]
            
                
            
            if current.getData(key) == None:
                
                current.addData(key, val)

                if varList.get(key) == None:

                    varList[key] = [val]

                else:

                    varList[key].append(val)
                
            
            else:
                

                print('MULTIPLE DECLARATION')
                return

 
        
        elif elt[0] == 'TYPEOF':
            
            key = elt[1]
            


            if varList.get(key) != None and len(varList[key]) > 0:

                print(varList[key][-1])

            else:

                print('UNDECLARED')

            
                    

                
            
           
        

quickScope()      





    
