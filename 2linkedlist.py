class Node:
    def __init__(self,data):
        self.item = data
        self.ref = None

class LinkedListHT:
    def __init__(self):      
        self.start_node = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.start_node is None:
            self.start_node = self.tail = new_node
            return

        self.tail.ref = new_node
        self.tail = new_node

    #insert ditengah
    def insert_after_item(self, x, data):
        n = self.start_node

        while n is not None:
            if n.item == x:
                break
            n = n.ref

        if n is None:
            print("item tidak valid/ tidak ditemukan")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


            if new_node.ref is None:
                self.tail = new_node

    # Hapus ditengah
    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("Listkosong")
            return
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
        if self.start_node is None:
            self.tail = None
            return
        
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("item tidak valid/tidak ditemukan") 
        else:

            if n.ref == self.tail:
                self.tail = n

            n.ref = n.ref.ref

    def display(self):
        n = self.start_node
        while n is not None:
            print(n.item, end=" ->")   
            n = n.ref
        print("None")

print("\n=== 2: Single Linked List(Head & tail)===")

list2 = LinkedListHT()
list2. insert_at_end("10")
list2. insert_at_end("20")
list2. insert_at_end("40")
list2. insert_at_end("50")

print("Awal:")
list2.display()

list2.insert_after_item("20", "30")
print()
print("setelah insert 30:")
list2.display()

list2.delete_element_by_value("30")
print()
print("setelah delete 30:")
list2.display()


