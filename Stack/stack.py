class Stack:
    stack: list

    def __init__(self):
        self.stack = []

    def push(self):
        while True:
            item = input("Insert a value or press Enter for exit: ")
            if item != '':            
                self.stack.append(item)
            else:
                break
        return self.stack

    def pop(self):
        self.stack.pop()
        return self.stack

    def clear(self):
        self.stack.clear()
        return self.stack


ex1 = Stack()
ex2 = Stack()


ex1.push()
print('Стэк 1: ', ex1.stack)
ex1.pop()
print('Стэк 1: ', ex1.stack)
ex1.clear()
print('Стэк 1: ', ex1.stack)
ex2.push()
print('Стэк 2: ', ex2.stack)


def main():
    pass


if __name__ == "__main__":
    main()
