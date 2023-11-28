class Stack:
    stack: list

    def __init__(self):
        self.stack = []

    def push(self):
        item1 = input("Insert a value: ")
        item2 = input("Insert a value: ")
        item3 = input("Insert a value: ")
        self.stack.append(item1)
        self.stack.append(item2)
        self.stack.append(item3)
        return self.stack

    def pop(self):
        self.stack.pop()
        return self.stack

    def clear(self):
        for _ in range(len(self.stack)):
            self.stack.pop()
        return self.stack

    def clear_rev(self):
        for _ in reversed(self.stack):
            self.stack.pop()
        return self.stack


def process_stack():
    pStack = Stack()
    pStack.push()
    print(pStack.stack)
    pStack.pop()
    print(pStack.stack)
    print(len(pStack.stack))
    pStack.clear()
    print(pStack.stack)


def main():
    process_stack()


if __name__ == "__main__":
    main()
