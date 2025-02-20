'''create linkd list take input from user'''

class node:
    def __init__(self,data):
        self.data= data
        self.next= None
        
        
        
def createList():
    size=int(input('enter the num of linked list: '))
    if size <=0:
        print('The linked list must have at least one node.')
        return None
    
    first_data = int(input('enter element 1: '))
    head = node(first_data)
    create_node= head
    
    for i in range(2,size+1):
        data = int(input(f"enter element {i}: "))
        new_node = node(data)  
        create_node.next=new_node
        create_node=new_node  
    return head    

def printkoro(head):
    currentNode= head
    while currentNode:
            print(currentNode.data,end='->')
            currentNode=currentNode.next
    print("Null")
    
    
head= createList()
if head:
    print("The linked list is: \n")
    printkoro(head)    