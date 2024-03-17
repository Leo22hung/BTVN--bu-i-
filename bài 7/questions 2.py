class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, value):
        self.main_stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.main_stack:
            return "Stack is empty"
        popped_element = self.main_stack.pop()
        if popped_element == self.min_stack[-1]:
            self.min_stack.pop()
        return popped_element

    def min(self):
        if not self.min_stack:
            return "Stack is empty"
        return self.min_stack[-1]

stack = MinStack()
stack.push(5)
stack.push(3)
stack.push(7)
print("Min element:", stack.min()) 
print("Min element after pop:", stack.min())  
stack.push(2)
print("Min element after push:", stack.min())  
