from CodingCraze.Stack.stack import Stack


def test_empty():
    stack = Stack()
    assert stack.empty() is True
    assert stack.size() == 0


def test_not_empty():
    stack = Stack()
    stack.push(42)
    assert stack.empty() is False
    assert stack.size() == 1


def test_clear():
    stack = Stack()
    stack.push(42)
    stack.clear()
    assert stack.empty() is True
    assert stack.size() == 0


def test_push_pop_one_value():
    stack = Stack()
    stack.push(42)
    assert stack.pop() == 42
    assert stack.empty() is True
    assert stack.size() == 0


def test_push_pop_several_values():
    stack = Stack()
    stack.push(42)
    stack.push(41)
    assert stack.size() == 2
    assert stack.pop() == 41
    assert stack.empty() is False
    assert stack.size() == 1


def test_two_stacks():
    a = Stack()
    b = Stack()
    a.push(1)
    a.push(2)
    a.push(3)
    b.push(42)
    b.push(41)
    b.push(40)
    assert a.size() == 3
    assert b.size() == 3
    assert a.pop() == 3
    assert b.pop() == 40


def test_print(capfd):
    stack = Stack()
    stack.push(42)
    stack.push(41)
    stack.push(40)
    stack.print()
    out, err = capfd.readouterr()
    assert out == "[42, 41, 40]\n"
