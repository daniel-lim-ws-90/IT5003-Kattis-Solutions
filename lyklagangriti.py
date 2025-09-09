# Initialise the Node
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
# Class for doubly Linked List
class doublyLinkedList:

    
    def __init__(self):
        self.start_node = None
        self.cursor = None
        self.maxSize = 0
        self.counter = 0

    # Insert Element to Empty list

    def InsertToEmptyList(self, data):
        if self.start_node is None:
            #print('Insert at Empty')
            new_node = Node(data)
            self.start_node = new_node
            self.cursor = new_node
            self.maxSize = 1
            self.counter = 1
            #print(self.cursor.item)
    

    # Insert element at the end
    def InsertAtEnd(self, data):
        
        # Check if the list is empty
        if self.start_node is None:

            new_node = Node(data)
            self.start_node = new_node
            self.cursor = new_node
            self.maxSize = 1
            self.counter = 1
            #print(str(self.cursor))
            #print(str(self.cursor.item))
            
        #n = self.start_node
        # Iterate till the next reaches NULL
        #while n.next is not None:
            #n = n.next
        else:
            #print(str(self.cursor))
            #print(str(self.cursor.item))
            #print('Insert at End')
            new_node = Node(data)
            self.cursor.next = new_node
            #print(str(self.cursor))
            #print(str(self.cursor.next))
            new_node.prev = self.cursor
            self.cursor = new_node
            self.maxSize += 1
            self.counter += 1
            #print(str(self.cursor))
            #print(str(self.cursor.item))
        

    def InsertAtStart(self, data):
        
        # Check if the list is empty
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            self.cursor = new_node
            self.maxSize = 1
            self.counter = 1
            #print(str(self.cursor))
            #print(str(self.cursor.item))
            
        #n = self.start_node
        # Iterate till the next reaches NULL
        #while n.next is not None:
            #n = n.next
        else:
            #print(str(self.cursor))
            #print(str(self.cursor.item))
            #print('Insert at start')
            new_node = Node(data)
            self.start_node.prev = new_node
            self.start_node = new_node
            #print(str(self.cursor))
            #print(str(self.cursor.prev))
            new_node.next = self.cursor
            self.cursor = new_node
            self.maxSize += 1
            self.counter += 1
            #print(str(self.cursor))
            #print(str(self.cursor.item))



    def InsertNode(self, data):

        

        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            self.cursor = new_node
            self.maxSize = 1
            self.counter = 1
            #print(str(self.cursor))
            #print(str(self.cursor.item))

        elif self.cursor.next is not None and self.counter > 0:
        
            #print(str(self.cursor))
            #print(str(self.cursor.item))
            #print('Insert at middle')
            new_node = Node(data)
            self.cursor.next.prev = new_node
            new_node.next = self.cursor.next
            new_node.prev = self.cursor
            self.cursor.next = new_node
            self.cursor = new_node
            self.maxSize += 1
            self.counter += 1
            #print(str(self.cursor))
            #print(str(self.cursor.item))

        elif self.cursor.next is not None and self.counter == 0:

            #print(str(self.cursor))
            #print(str(self.cursor.item))
            #print('Insert at start')
            new_node = Node(data)
            self.start_node.prev = new_node
            self.start_node = new_node
            #print(str(self.cursor))
            #print(str(self.cursor.prev))
            new_node.next = self.cursor
            self.cursor = new_node
            self.maxSize += 1
            self.counter += 1
            #print(str(self.cursor))
            #print(str(self.cursor.item))

        elif self.cursor.next is None and self.counter > 0:

            #print(str(self.cursor))
            #print(str(self.cursor.item))
            #print('Insert at End')
            new_node = Node(data)
            self.cursor.next = new_node
            #print(str(self.cursor))
            #print(str(self.cursor.next))
            new_node.prev = self.cursor
            self.cursor = new_node
            self.maxSize += 1
            self.counter += 1
            #print(str(self.cursor))
            #print(str(self.cursor.item))

        elif self.cursor.next is None and self.counter == 0:

            #print(str(self.cursor))
            #print(str(self.cursor.item))
            #print('Insert at start')
            new_node = Node(data)
            self.start_node.prev = new_node
            self.start_node = new_node
            #print(str(self.cursor))
            #print(str(self.cursor.prev))
            new_node.next = self.cursor
            self.cursor = new_node
            self.maxSize += 1
            self.counter += 1
            #print(str(self.cursor))
            #print(str(self.cursor.item))

            


        
        
    def DeleteAtEnd(self):
        # Check if the List is empty
        if self.start_node is None:
            print("The Linked list is empty, no element to delete")
            return -1
        if self.cursor is not None and self.cursor.next is None and self.counter > 0:
            self.cursor.prev.next = None
            temp = self.cursor.prev
            del self.cursor
            self.cursor = temp
            self.maxSize -= 1
            self.counter -= 1
            return
        
        
        
    # Traversing and Displaying each element of the list

    def DeleteAtStart(self):

        if self.start_node is None:
            #print("The Linked list is empty, no element to delete")
            return -1
        elif self.cursor is not None and self.cursor.prev is None:
            self.cursor.next.prev = None
            self.start_node = self.cursor.next
            temp = self.cursor.next
            del self.cursor
            self.cursor = temp
            self.maxSize -= 1
            return



    def DeleteNode(self):
         

        if self.start_node is None:

            #print("The Linked list is empty, no element to delete")
            return -1

        elif self.cursor == self.start_node and self.cursor.next is None:

            #print("del " + str(self.cursor.item))

            self.cursor = None
            self.start_node = None
            self.maxSize = 0
            self.counter = 0
            

        elif self.cursor.prev is not None and self.cursor.next is not None and self.counter > 0:

            #print("mid del " + str(self.cursor.item))


            self.cursor.prev.next = self.cursor.next
            self.cursor.next.prev = self.cursor.prev
            temp = self.cursor.prev

            self.cursor.next = None
            self.cursor.prev = None
            del self.cursor

            self.cursor = temp
            self.maxSize -= 1
            self.counter -= 1

        elif self.cursor.prev is not None and self.cursor.next is None and self.counter > 0 :

            #print("end del " + str(self.cursor.item))

            self.cursor.prev.next = None
            temp = self.cursor.prev
            del self.cursor
            self.cursor = temp
            self.maxSize -= 1
            self.counter -= 1


        elif self.cursor.prev is None and self.cursor.next is not None and self.counter > 0:

            #print("start del " + str(self.cursor.item))


            self.cursor.next.prev = None
            self.start_node = self.cursor.next
            temp = self.cursor.next
            del self.cursor
            self.cursor = temp
            self.maxSize -= 1
            self.counter -= 1

            
        
    

    
    def moveLeft(self):
        if self.start_node is None:
            print("The list is empty")
            return -1
        elif self.cursor is not None and self.cursor.prev is None and self.counter > 0:
            #n = self.start_node
            #while n is not None:
            #print("Element is: ", n.item)
            #n = n.next
            self.counter -= 1
            
        elif self.cursor is not None and self.cursor.prev is not None and self.counter > 0:

            self.counter -= 1
            self.cursor = self.cursor.prev
            #print("Left " +str(self.cursor.item))

    def moveRight(self):

        if self.start_node is None:
            print("The list is empty")
            return -1
        
        elif self.cursor is not None and self.cursor.next is not None and self.counter < self.maxSize:

            self.cursor = self.cursor.next
            self.counter += 1
            #print("Right " + str(self.cursor.item))

    
    def Display(self):

        #print(self.maxSize)
        #print(self.start_node)
        #print(self.start_node.next)

        if self.start_node is None:
           
            return

        else:
            n = self.start_node
            array = []
            
            while n is not None:
                #print(str(n))
                #print((str(n.item)).strip())
                array.append(n.item)
                n = n.next
                #print(str(n))
                
            print(''.join(array))
            


# Create a new Doubly Linked List
#NewDoublyLinkedList = doublyLinkedList()
# Insert the element to empty list
#NewDoublyLinkedList.InsertToEmptyList(10)
# Insert the element at the end
#NewDoublyLinkedList.InsertToEnd(20)
#NewDoublyLinkedList.InsertToEnd(30)
#NewDoublyLinkedList.InsertToEnd(40)
#NewDoublyLinkedList.InsertToEnd(50)
#NewDoublyLinkedList.InsertToEnd(60)
# Display Data
#NewDoublyLinkedList.Display()
# Delete elements from start
#NewDoublyLinkedList.DeleteAtStart()
# Delete elements from end
#NewDoublyLinkedList.DeleteAtStart()
# Display Data
#NewDoublyLinkedList.Display()

string = str(input())
T = len(string)
wordStack = doublyLinkedList()

    
for character in string:


    if character != 'B' and character != 'L' and character != 'R':

        wordStack.InsertNode(character)
        
        
    elif  character == 'B' :
            
        wordStack.DeleteNode()
        
        
        
    elif character == 'L':

        wordStack.moveLeft()  
        
            
    elif character == 'R' :
            
        wordStack.moveRight()    
        
        

wordStack.Display()    
#print(''.join(wordStack))
