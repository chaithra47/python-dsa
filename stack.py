class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
        print(f"pushed: {item}")
    
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        print(f"Popped: {self.stack.pop()}")
    
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print(self.stack)

s = Stack()
s.push(400)
s.push(300)
s.push(500)
s.push(600)
s.pop()  
print(s.size())  
print(s.peek())  
s.display()  
