from dataclasses import dataclass


@dataclass
class Node:
    value: any = None
    next: any = None


@dataclass
class List:
    size: int = 0
    value: any = None
    head: Node = Node()


def list_print(list):
    ls_copy = list.head
    arr = []
    while ls_copy.next:
        arr.append(ls_copy.value)
        ls_copy = ls_copy.next
    arr.append(ls_copy.value)
    print(arr)


def create():
    return List()


def head(list):
    return list.head.value


def insert(list, value, index):
    if index > list.size:
        return
    if list.size == 0 == index:
        list.head.value = value
    else:
        list_copy = list.head
        for i in range(index - 1):
            list_copy = list_copy.next
        tail = list_copy.next
        list_copy.next = Node(value, tail)
    list.size += 1


def tail(list):
    list_copy = list.head
    for i in range(list.size - 1):
        list_copy = list_copy.next
    return list_copy.value


def locate(list, value):
    list_copy = list.head
    for i in range(list.size):
        if list_copy.value == value:
            return i
        list_copy = list_copy.next


def retrieve(list, index):
    list_copy = list.head
    if index >= list.size:
        return
    for i in range(index):
        list_copy = list_copy.next
    return list_copy.value


def delete(list, index):
    if index == 0:
        list.head = list.head.next
    else:
        list_copy = list.head
        for i in range(index - 1):
            list_copy = list_copy.next
        tail = list_copy.next
        tail = tail.next
        list_copy.next = tail
