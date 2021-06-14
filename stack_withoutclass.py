def create_stack():
    stack = []
    return stack 
def empty_stack(stack):
    if(len(stack)==0):
        return 0
def push(stack,element):
    stack.append(element)
    return stack
def pop(stack,item):
    if(empty_stack(stack)):
        return "stack is empty"
    else:
        return stack.pop()
stack=create_stack()
push(stack,str(4))
push(stack,str(6))
push(stack,str(5))
print("pop element from stack:"+pop(stack,4))
print(stack)
