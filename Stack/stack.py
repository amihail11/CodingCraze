class Stack:
    def __init__(self):
        self.stack = []

    def push_stack(self):
        item1 = input("Insert a value or press 'Enter' for exit: ")
        item2 = input("Insert a value or press 'Enter' for exit: ")
        item3 = input("Insert a value or press 'Enter' for exit: ")
        self.stack.append(item1)
        self.stack.append(item2)
        self.stack.append(item3)
        return self.stack
                            
    def pop_stack(self):
        self.stack.pop()
        return self.stack
    
    def remove_items(self):
        for i in range(len(self.stack)):
            if i is None:
                break
            else:
                self.stack.pop()
                i = i-1
        return self.stack
               
    
stack_class = Stack()

        
def start_class():
    stack_class.push_stack()
    print(stack_class.stack)
    stack_class.pop_stack()
    print(stack_class.stack)
    print(len(stack_class.stack))
    stack_class.remove_items()
    print(stack_class.stack)


def main():
    start_class()

if __name__ == "__main__":
    main()
