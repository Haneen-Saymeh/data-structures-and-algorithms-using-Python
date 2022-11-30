class Node:
    def __init__(self, value):
        self.value= value
        self.next= None

class Linkedlist:
    def __init__(self):
        self.head= None


    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value) 
            current= current.next

    def add_to_head(self, value):
        newNode= Node(value)
        if self.head is None:
            self.head= newNode
        else:
            current = Node(value)
            current.next= self.head
            self.head= current

    def delete_head(self):
        



list1 = Linkedlist()
list1.head=Node("Tony Stark")
list1.head.next= Node("Thor")
list1.head.next.next=Node("Winter soldier")
list1.add_to_head("Thanos")
list1.traverse()