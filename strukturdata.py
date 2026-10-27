class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.start_node is None :
            self.start_node = new_node
            return

        n = self.start_node
        while n.ref is not None :
            n = n.ref

        n.ref = new_node

    # Insert di tengah     
    def insert_after_item(self, x, data):
        n = self. start_node

        while n is not None :
            if n.item == x :
                break
            n = n.ref

        if n is None:
            print("item tidak valid/ tidak ditemukan")
        else :
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node   

    # Hapus ditengah
    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("List kosong")
            return
        
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return

        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("item tidak valid/ tidak ditemukan")
        else:
            n.ref = n.ref.ref

    def display(self):
        n = self.start_node
        while n is not None:
            print(n.item, end=" ->")
            n = n.ref
        print("None")

print("\n=== 1 : Single Linked list (HEAD)===")


list1 = LinkedList()
list1.insert_at_end("10")
list1.insert_at_end("20")
list1.insert_at_end("40")
list1.insert_at_end("50")


print("Awal:")
list1.display()

list1.insert_after_item("20", "30")
print()
print("Setelah insert 30:")
list1.display()

list1.delete_element_by_value("30")
print()
print("Setelah delete 30:")
list1.display()