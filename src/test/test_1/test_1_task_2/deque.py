from dataclasses import dataclass
from typing import TypeVar, Generic, Optional

Value = TypeVar("Value")


@dataclass
class Node(Generic[Value]):
    value: Value
    previous: Optional["Node[Value]"] = None
    next: Optional["Node[Value]"] = None


@dataclass
class Deque(Generic[Value]):
    size: int = 0
    tail: Optional["Node[Value]"] = None
    head: Optional["Node[Value]"] = None


def display(deque: Deque) -> None:
    deque_elements = []
    front_node = deque.head
    while front_node:
        deque_elements.append(str(front_node.value))
        front_node = front_node.next
    print(" -> ".join(deque_elements))


def create_deque() -> Deque:
    return Deque()


def size(deque: Deque) -> int:
    return deque.size


def is_empty(deque: Deque) -> bool:
    return deque.size == 0


def popFront(deque: Deque) -> Value:
    if is_empty(deque):
        raise ValueError("Deque пуст")
    value = deque.head.value
    deque.head = deque.head.next
    deque.size -= 1
    return value


def popBack(deque: Deque) -> Value:
    if is_empty(deque):
        raise ValueError("Deque пуст")
    value = deque.tail.value
    back_node = deque.tail
    back_node.previous.next = None
    deque.tail = back_node.previous
    deque.size -= 1
    return value


def push_empty(deque: Deque, value: Value) -> None:
    new_node = Node(value)
    deque.head = new_node
    deque.tail = new_node


def pushFront(deque: Deque, value: Value) -> None:
    if is_empty(deque):
        push_empty(deque, value)
    else:
        front_node = deque.head
        new_node = Node(value, None, front_node)
        front_node.previous = new_node
        deque.head = new_node
    deque.size += 1


def pushBack(deque: Deque, value: Value) -> None:
    if is_empty(deque):
        push_empty(deque, value)
    else:
        back_node = deque.tail
        new_node = Node(value, back_node, None)
        back_node.next = new_node
        deque.tail = new_node
    deque.size += 1
