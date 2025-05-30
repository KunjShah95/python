# Node class
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

# Example usage
dll = DoublyLinkedList()
dll.insert_at_end(100)
dll.insert_at_end(200)
dll.insert_at_end(300)
dll.display_forward()   # 100 <-> 200 <-> 300 <-> None
dll.display_backward()  # 300 <-> 200 <-> 100 <-> None
