from dataclasses import dataclass


@dataclass
class Node:
    value: any = None
    next: any = None


@dataclass
class List:
    size: int = 0
    head: Node = None


def create():
    return List()


def head(list):
    if list.size == 0:
        raise ValueError("Список пуст и у него нет первого элемента")
    return list.head.value


def tail(list):
    if list.size == 0:
        raise ValueError("Список пуст и у него нет последнего элемента")
    list_copy = list.head
    for i in range(list.size - 1):
        list_copy = list_copy.next
    return list_copy.value


def insert(list, value, index):
    if index > list.size or index < 0:
        return False
    if list.size == 0 == index:
        list.head = Node(value)
    else:
        list_copy = list.head
        for i in range(index - 1):
            list_copy = list_copy.next
        tail = list_copy.next
        list_copy.next = Node(value, tail)
    list.size += 1
    return True


def locate(list, value):
    list_copy = list.head
    for i in range(list.size):
        if list_copy is None:
            return
        if list_copy.value == value:
            return i
        list_copy = list_copy.next


def retrieve(list, index):
    list_copy = list.head
    if index >= list.size or index < 0:
        return
    for i in range(index):
        list_copy = list_copy.next
    return list_copy.value


def delete(list, index):
    if list.size == 0 or index >= list.size:
        return False
    if index == 0:
        list.head = list.head.next
    else:
        list_copy = list.head
        for i in range(index - 1):
            list_copy = list_copy.next
        tail = list_copy.next
        tail = tail.next
        list_copy.next = tail
    return True
