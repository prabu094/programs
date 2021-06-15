class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()
 
    def is_empty(self):
        return self.inbox.is_empty() and self.outbox.is_empty()
 
    def enqueue(self, data):
        self.inbox.push(data)
 
    def dequeue(self):
        if self.outbox.is_empty():
            while not self.inbox.is_empty():
                popped = self.inbox.pop()
                self.outbox.push(popped)
        return self.outbox.pop()
 
 
class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
 
queue1 = Queue()
while True:
    print('		*******************MENU*********************************')
    print('		1. Enqueue <Value>')
    print('		2. Dequeue')
    print('		3. Quit')
    print('		********************************************************')
    do = input('		Enter Your Choice (& value in enqueue only): ').split()
 
    operation = do[0].strip().lower()
    if operation == 'Enqueue' or operation == '1' or operation == 'enqueue':
        queue1.enqueue(int(do[1]))
    elif operation == 'Dequeue' or operation == '2' or operation == 'dequeue':
        if queue1.is_empty():
            print('		>> Queue is empty.')
        else:
            dequeued = queue1.dequeue()
            print('		Dequeued element is : ', int(dequeued))
    elif operation == 'quit' or operation == '3' or operation == 'Quit':
        break
    else:
        print("		Invalid Option:")
