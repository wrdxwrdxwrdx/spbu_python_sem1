from dataclasses import dataclass
from collections import namedtuple


StackElement = namedtuple("StackElement", ["value", "next"])


@dataclass
class Stack:
    size: int = 0
    head: StackElement = None


def create_stack():
    return Stack()


def push(stack, value):
    stack.head = StackElement(value, stack.head)
    stack.size += 1


def pop(stack):
    if not empty(stack):
        stack.head = stack.head.next
        stack.size -= 1
        return True
    else:
        return False


def top(stack):
    if not empty(stack):
        return stack.head.value
    else:
        return False


def size(stack):
    return stack.size


def empty(stack):
    return size(stack) == 0


def main():
    new_stack = create_stack()
    pop(new_stack)
    top(new_stack)
    push(new_stack, 3)
    push(new_stack, 2)
    push(new_stack, 1)
    push(new_stack, 4)
    push(new_stack, 5)
    pop(new_stack)
    print(f"top element = {top(new_stack)}")
    print(f"size: {size(new_stack)}")
    print(f"is stack empty: {empty(new_stack)}")


if __name__ == "__main__":
    main()
