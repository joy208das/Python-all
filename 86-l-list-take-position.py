class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to create a linked list from user input
def create_linked_list():
    num_nodes = int(input("Enter the number of nodes: "))
    if num_nodes <= 0:
        print("The linked list must have at least one node.")
        return None
    
    data = int(input("Enter data for node 1: "))
    head = Node(data)
    current_node = head

    for i in range(2, num_nodes + 1):
        data = int(input(f"Enter data for node {i}: "))
        new_node = Node(data)
        current_node.next = new_node
        current_node = new_node

    return head

# Function to insert a node at a given position
def insert_at_position(head, newNode, position):
    # Case: Insert at the beginning (position 1)
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    current_position = 1

    # Traverse to the node just before the desired position
    while currentNode is not None and current_position < position - 1:
        currentNode = currentNode.next
        current_position += 1

    # Check if the position is valid
    if currentNode is None:
        print("Position out of range.")
        return head

    # Insert the new node at the desired position
    newNode.next = currentNode.next
    currentNode.next = newNode
   
    return head

# Function to print the linked list
def print_linked_list(head):
    current_node = head
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("null")

# Main code
# Main code
head = create_linked_list()
if head:
    print("The initial linked list is:")
    print_linked_list(head)

    # Get new data and position from user
    new_data = int(input("Enter the data for the new node: "))
    position = int(input("Enter the position to insert the new node: "))
    new_node = Node(new_data)  # Create a new Node instance

    head = insert_at_position(head, new_node, position)
    print("The linked list after insertion is:")
    print_linked_list(head)
  