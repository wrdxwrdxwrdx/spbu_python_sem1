from dataclasses import dataclass
from collections import namedtuple


StackElement = namedtuple("StackElement", ["value", "next"])


@dataclass
class Stack:
    size: int
    head: StackElement = None


def create_stack():
    stack = Stack(size=0)
    return stack


def push(stack, value):
    stack.head = StackElement(value, stack.head)
    stack.size += 1


def pop(stack):
    stack.head = stack.head.next
    stack.size -= 1


def top(stack):
    return stack.head.value


def size(stack):
    return stack.size


def empty(stack):
    return bool(stack.size)


def main():
    new_stack = create_stack()
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
