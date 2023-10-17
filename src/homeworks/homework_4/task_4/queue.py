from dataclasses import dataclass


@dataclass
class Node:
    value: any
    next: any


@dataclass
class Queue:
    max_size: int = 10
    size: int = 0
    head: Node = None
    tail: Node = None


def create_queue():
    return Queue()


def enqueue(queue, value):
    if is_full(queue):
        return False
    if is_null(queue):
        queue.head = Node(value, None)
        queue.tail = queue.head
        queue.size += 1
    else:
        queue.tail.next = Node(value, None)
        queue.tail = queue.tail.next
        queue.size += 1
    return True


def dequeue(queue):
    if is_null(queue):
        return False
    queue.size -= 1
    queue.head = queue.head.next
    return True


def is_full(queue):
    return queue.size == queue.max_size


def is_null(queue):
    return queue.size == 0


def peek(queue):
    return queue.head.value
