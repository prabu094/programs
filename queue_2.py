class Queue:
    def __init__(self, capacity):
        self.front = -1
        self.rear = -1
        self.capacity = capacity
        self.curr_size = 0
        self.capacity = capacity
        self.Q = [None] * capacity

    def isFull(self):
        return self.rear == self.capacity - 1

    def enqueue(self, item):
        if self.isFull():
            print("FULL")
            return

        if self.front == -1:
            self.front = 0

        self.rear += 1
        self.Q[self.rear] = item
        self.curr_size += 1

        print("{} was enqueued".format(item))

    def isEmpty(self):
        return self.front == -1

    def dequeue(self):
        if self.isEmpty():
            print("EMPTY")
            return

        print("{} was dequeued".format(str(self.Q[self.front])))
        self.front += 1
        self.curr_size -= 1
        if self.front > self.rear:
            self.front = self.rear = -1


    def display(self):
        if self.isEmpty():
            print("EMPTY")
            return
        for item in range(self.front, self.rear + 1):
            print("{}".format(self.Q[item]), end=" ")


queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.display()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.display()
