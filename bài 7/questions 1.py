class ThreeStacks:
    def __init__(self, size):
        self.size = size
        self.list = [None] * (size * 3)
        self.indices = [0, size, size * 2]  # Chỉ mục bắt đầu của mỗi stack

    def push(self, stack_num, value):
        if self.is_full(stack_num):
            print(f"Stack {stack_num} is full")
        else:
            self.list[self.indices[stack_num - 1]] = value
            self.indices[stack_num - 1] += 1

    def pop(self, stack_num):
        if self.is_empty(stack_num):
            print(f"Stack {stack_num} is empty")
        else:
            self.indices[stack_num - 1] -= 1
            return self.list[self.indices[stack_num - 1]]

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            print(f"Stack {stack_num} is empty")
        else:
            return self.list[self.indices[stack_num - 1] - 1]

    def is_empty(self, stack_num):
        return self.indices[stack_num - 1] == (stack_num - 1) * self.size

    def is_full(self, stack_num):
        return self.indices[stack_num - 1] == stack_num * self.size


# Example usage:
three_stacks = ThreeStacks(3)

three_stacks.push(1, 1)
three_stacks.push(2, 2)
three_stacks.push(3, 3)

print("Stack 1 peek:", three_stacks.peek(1))
print("Stack 2 peek:", three_stacks.peek(2))
print("Stack 3 peek:", three_stacks.peek(3))

print("Pop from Stack 1:", three_stacks.pop(1))
print("Pop from Stack 2:", three_stacks.pop(2))
print("Pop from Stack 3:", three_stacks.pop(3))

print("Is Stack 1 empty?", three_stacks.is_empty(1))
print("Is Stack 2 empty?", three_stacks.is_empty(2))
print("Is Stack 3 empty?", three_stacks.is_empty(3))
