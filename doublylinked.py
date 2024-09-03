class Node:
    def __init__(self, data):
        self.data = data  # Data to be stored in the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
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
            new_node.prev = current  # Link the new node back to the last node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:  # If the list is not empty
            self.head.prev = new_node  # Link the current head back to the new node
            new_node.next = self.head  # Link the new node to the current head
        self.head = new_node  # Update the head to the new node

    def delete_node(self, key):
        current = self.head

        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            if self.head:
                self.head.prev = None  # Update the previous pointer of the new head
            current = None
            return

        # Search for the node to be deleted
        while current and current.data != key:
            current = current.next

        # If the key was not found
        if not current:
            print("Node with data", key, "not found.")
            return

        # Unlink the node from the linked list
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next
        current = None

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.head
        while current and current.next:
            current = current.next  # Move to the end of the list

        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Testing the DoublyLinkedList implementation

# Create a new doubly linked list
dll = DoublyLinkedList()

# Insert elements
dll.insert_at_end(1)
dll.insert_at_end(2)
dll.insert_at_end(3)

# Traverse the list forward
print("Doubly linked list after inserting 1, 2, 3 at the end (forward traversal):")
dll.traverse_forward()

# Traverse the list backward
print("Doubly linked list after inserting 1, 2, 3 at the end (backward traversal):")
dll.traverse_backward()

# Insert at the beginning
dll.insert_at_beginning(0)
print("Doubly linked list after inserting 0 at the beginning (forward traversal):")
dll.traverse_forward()

# Delete a node
dll.delete_node(2)
print("Doubly linked list after deleting node with data 2 (forward traversal):")
dll.traverse_forward()

# Traverse the list backward after deletion
print("Doubly linked list after deleting node with data 2 (backward traversal):")
dll.traverse_backward()

# Attempt to delete a non-existent node
dll.delete_node(4)
