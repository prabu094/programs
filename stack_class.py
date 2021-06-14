class Stack:
    def __init__(self, size):
        self.max_size = size
        self.stack = []

    def is_full(self):
        if len(self.stack) == self.max_size:
            print("Overflow Condition, can't insert further")
        return len(self.stack) == self.max_size

    def is_empty(self):
        if len(self.stack) == 0:
            print("Underflow Condition, can't pop further")
        return len(self.stack) == 0

    def push(self, val):
        if self.is_full():
            return
        self.stack.append(val)
        print("The Value {} has been pushed".format(val))

    def peek(self):
        if len(self.stack) == 0:
            print("Nothing to print, the stack is underflow condition!")
            return
        print("Peek : ", self.stack[-1])

    def pop(self):
        if self.is_empty():
            return
        temp = self.stack.pop()
        print("{} has been popped from the stack ".format(temp))


if __name__ == '__main__':
    s = Stack(5)
    s.push(3)
    s.push(2)
    s.push(1)
    s.pop()
    s.peek()
    s.pop()
    s.peek()
    s.pop()
