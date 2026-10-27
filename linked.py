class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def display(self):
        temp = self.start_node
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.ref
        print("None")

# testing
ll = LinkedList()
ll.insert_at_start(10)
ll.insert_at_start(20)
ll.insert_at_start(30)

ll.display()