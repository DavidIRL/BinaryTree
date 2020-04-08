class Stack():

    def __init__(self):
        self.values = []
        
    def push(self, value):
        self.values.append(value)
        
    def pop(self):
        if self.size() == 0:
            return None
        return self.values.pop()

    def top(self):
        if len(self.values) > 0:
            return self.values[-1]
        else:
            return None

    def is_empty(self):
        return len(self.values) == 0

    def __repr__(self):
        if len(self.values) > 0:
            output = "\n"
            output += "\n".join([str(item) for item in self.values[::-1]])
            return output
        else:
            return 'Stack is empty'

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    stack.push(60)
    print(stack)
    print('\n')
    print(stack.pop())
    print('\n')
    print(stack)