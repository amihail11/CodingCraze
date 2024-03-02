class Stack:
    """Описание класса стэка"""

    stack:list
    
    def __init__(self, stack=[], value=None) -> None:
        """инициализирует атрибуты класса"""
        self.stack = stack
        self.value = value

    def push(self) -> list:
        """добавляет значение в список"""
        self.stack.append(self.value)
        return self.stack
    
    def pop(self) -> list:
        """удаляет последний элемент списка"""
        self.stack.pop()
        return self.stack
    
    def show_length(self) -> None:
        """выводит длину списка"""
        print(len(self.stack))
    
    def clear(self) -> list:
        """очищает список"""
        self.stack.clear()
        return self.stack
    
    def print(self) -> None:
        """выводит список на экран"""
        print(self.stack)

ex = Stack(value=345)
ex.push()
ex = Stack(value=1.234)
ex.push()
ex.print()
ex = Stack(value='ad234')
ex.push()
ex.print()
ex.show_length()
ex.pop()
ex.print()
ex.clear()
ex.print()


def main():
    pass


if __name__ == "__main__":
    main()
