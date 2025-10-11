class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0
        self.rear = -1
        self._size = 0
    
    def is_empty(self):
        return self._size == 0
    
    def is_full(self):
        return self._size == self.capacity
    
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")
        # wrap around using modulo
        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = item
        self._size += 1
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self.arr[self.front]
        # optional: clear the spot
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self._size -= 1
        return item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.arr[self.front]
    
    def size(self):
        return self._size
    
    def __str__(self):
        # printing elements from front to rear in order
        items = []
        idx = self.front
        for _ in range(self._size):
            items.append(repr(self.arr[idx]))
            idx = (idx + 1) % self.capacity
        return "CircularQueue(" + ", ".join(items) + ")"
