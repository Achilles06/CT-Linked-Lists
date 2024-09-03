class Node:
    def __init__(self, data):
        self.data = data  # Data to be stored in the node
        self.next = None  # Pointer to the next node in the list

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Link the last node to the new node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Update the head to the new node

    def delete_node(self, key):
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the node to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found
        if not current:
            print("Node with data", key, "not found.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Testing the SinglyLinkedList implementation

# Create a new singly linked list
sll = SinglyLinkedList()

# Insert elements
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)

# Traverse the list
print("Linked list after inserting 1, 2, 3 at the end:")
sll.traverse()

# Insert at the beginning
sll.insert_at_beginning(0)
print("Linked list after inserting 0 at the beginning:")
sll.traverse()

# Delete a node
sll.delete_node(2)
print("Linked list after deleting node with data 2:")
sll.traverse()

# Attempt to delete a non-existent node
sll.delete_node(4)
