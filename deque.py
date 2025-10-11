from collections import deque

class Queue:
    def __init__(self):
        self._dq = deque()
    
    def is_empty(self):
        return len(self._dq) == 0
    
    def enqueue(self, item):
        self._dq.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._dq.popleft()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._dq[0]
    
    def size(self):
        return len(self._dq)
    
    def __str__(self):
        return "Queue(" + ", ".join(repr(x) for x in self._dq) + ")"
