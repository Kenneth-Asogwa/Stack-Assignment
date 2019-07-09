
## This program will create a stack and allow the,
## user to perform push and pop operations on it

class Stack:
    def __init__(self):
        self.items = []
    ## we now define these methods below inside the class Stack
    def is_empty(self):
        return self.items == []

    def push(self, item):
         self.items.append(item)

    def pop(self):
        return self.items.pop()


new_stack = Stack() ##creates a new instance of Stack

while True:
    print('push <name>')
    print('pop')
    print('stop')

    do = input('Which action do you want to perform?: ').split()
    print(do)
    operation = do[0].strip().lower()
    if operation == 'push':
        new_stack.push(do[1])

    elif operation == 'pop':
        if new_stack.is_empty():
            print('Cannot pop, stack is empty.')

        else:
            print('Popped name: ', new_stack.pop())
    elif operation == 'stop':
        break
