class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
# Class for doubly Linked List
class doublyLinkedList:
    def __init__(self):
        self.start_node = None
        self.end_node = None
    # Insert Element to Empty list
    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            self.end_node = new_node
        
    # Insert element at the end
    def InsertToEnd(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            self.end_node = new_node
            return
        n = self.end_node
        # Iterate till the next reaches NULL
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n
        self.end_node = new_node

    def InsertToStart(self, data):
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            self.end_node = new_node
            return
        n = self.start_node
        # Iterate till the next reaches NULL
        new_node = Node(data)
        n.prev = new_node
        new_node.next = n
        self.start_node = new_node

    # Delete the elements from the start
    def DeleteAtStart(self):
        if self.start_node is None or self.end_node == None:
            print("error")
            #print("The Linked list is empty, no element to delete")
            return -1
        if self.end_node.prev is None or self.start_node.next == None:
            self.start_node = None
            self.end_node = None
            return 1
        self.start_node = self.start_node.next
        self.start_node.prev = None;
        return 1

    # Delete the elements from the end


    def DeleteAtEnd(self):
        # Check if the List is empty
        if self.start_node is None or self.end_node == None :
            print("error")
            #print("The Linked list is empty, no element to delete")
            return -1
        if self.end_node.prev is None or self.start_node.next == None:
            self.start_node = None
            self.end_node = None
            return 1
        self.end_node = self.end_node.prev
        self.end_node.next = None
        return 1
        
    # Traversing and Displaying each element of the list
    def Display(self):
        if self.start_node is None or self.end_node == None:
            print("[]")
            return
        else:


            ansArray = ['[']

            n = self.start_node
        
            while n is not None:

                if n.next is not None :
            
                    ansArray.append(n.item+',')
                    n = n.next

                else:

                    ansArray.append(n.item)
                    n = n.next
            
            
            
            ansArray.append(']')

            print(''.join(ansArray))


    def DisplayR(self):

        if self.end_node is None or self.start_node is None:
            print("[]")
            return
        else:


            ansArray = ['[']

            n = self.end_node
        
            while n is not None:

                if n.prev is not None :
            
                    ansArray.append(n.item)
                    ansArray.append(',')
                    n = n.prev

                else:

                    ansArray. append(n.item)
                    n = n.prev
            
            
            
            ansArray.append(']')

            print(''.join(ansArray))



testN = int(input())


for i in range(testN):
    
    #testArray = []
    linkList = doublyLinkedList()
    instruction = str(input())
    N = int(input())
    arrayString = str(input())

    if len(arrayString) == 2:

        arrayString = []


    else:

        arrayString = arrayString[1:len(arrayString)-1]
        arrayString = arrayString.split(',')
        #print(arrayString)


    front = True
    result = 1
    
    
    for elt in arrayString:
        
        #if elt != '[' and elt != ']' and elt != ',' :
            
        linkList.InsertToEnd(elt)


    for word in instruction:

        if word == 'R':

            front = not front


        elif word == 'D' and front == True  :

            result = linkList.DeleteAtStart()
            #print(result)
            if result < 0:
                break
            

        elif word == 'D' and front == False :

            result = linkList.DeleteAtEnd()
            #print(result)
            if result < 0:
                break


    if front == False and result > 0:

        linkList.DisplayR()

    elif front == True and result > 0:

        linkList.Display()
    