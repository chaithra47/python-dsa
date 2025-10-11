class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            # queue empty, new node is both front and rear
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            # queue is now empty
            self.rear = None
        self._size -= 1
        return value
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.front.value
    
    def size(self):
        return self._size
    
    def __str__(self):
        res = []
        curr = self.front
        while curr:
            res.append(repr(curr.value))
            curr = curr.next
        return "LinkedQueue(" + " -> ".join(res) + ")"
