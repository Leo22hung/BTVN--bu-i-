class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [[]]

    def push(self, value):
        if len(self.stacks[-1]) >= self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)

    def pop(self):
        if not self.stacks:
            print("SetOfStacks is empty")
            return None
        popped_value = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return popped_value

    def popAt(self, index):
        if index < 0 or index >= len(self.stacks):
            print("Invalid stack index")
            return None
        popped_value = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return popped_value


set_of_stacks = SetOfStacks(3) 
set_of_stacks.push(1)
set_of_stacks.push(2)
set_of_stacks.push(3)
set_of_stacks.push(4)
set_of_stacks.push(5)
set_of_stacks.push(6)

print("Pop:", set_of_stacks.pop())  
print("Pop from stack 0:", set_of_stacks.popAt(0))  
