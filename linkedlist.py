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
        temp = self.head
        self.head= self.head.next
        temp=None

    def length_of(self):
        current=self.head
        total=0
        while current is not None:
            total=total+1
            current= current.next
        return total
        

    
            



list1 = Linkedlist()
list1.head=Node("Tony Stark")
list1.head.next= Node("Thor")
list1.head.next.next=Node("Winter soldier")
list1.add_to_head("Thanos")
list1.traverse()
list1.delete_head()
list1.traverse()
print(list1.length_of())