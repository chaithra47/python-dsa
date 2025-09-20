class Node:
    def __init__(self,data):
        self.data = data
        self.next = None   

class SLL:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("list is empty")
            return
        print("Deleted:",self.head.data)
        self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head.next is None:
            print("Deleted:",self.head.data)
            self.head = None
            return
        prev = self.head
        curr = self.head.next
        while curr.next:
            prev = curr
            curr = curr.next  
        print("deleted:",curr.data)
        prev.next = None

    def delete_at_pos(self,pos):
        if self.head is None:
            print("list is empty")
            return 
        if pos==1:
            print("Deleted:",self.head.data)
            self.head = self.head.next
            return
        curr = self.head
        prev = None
        count = 1
        while curr and count < pos:
            prev = curr
            curr = curr.next
            count += 1 
        if curr is None:
            print("Invalid position")
            return 
        print("Deleted:",curr.data)
        prev.next = curr.next 
    def display(self):
        if self.head is None:
            print("list is empty")
            return                 
        curr = self.head
        while curr:
            print(curr.data,end="->")
            curr = curr.next
        print("None")

ll = SLL()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.display()          
ll.delete_at_beginning()
ll.display()
ll.delete_end()
ll.display()
ll.delete_at_pos(2)
ll.display()  
