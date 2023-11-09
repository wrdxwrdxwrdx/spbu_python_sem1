from dataclasses import dataclass, field
from typing import TypeVar, Optional, Generic

Key = TypeVar("Key")
Value = TypeVar("Value")


@dataclass
class HashTable(Generic[Value]):
    values: list[Optional[Value]] = field(
        default_factory=lambda: [[] for _ in range(16)]
    )
    keys_number: int = 0
    capacity: int = 16


def hash_function(key: Key, capacity: int) -> int:
    output = 0
    for char in str(key):
        output += ord(char)
    return output % capacity


def get_load_factor(hash_table: HashTable) -> float:
    load_factor = hash_table.keys_number / hash_table.capacity
    return load_factor


def resize(hash_table: HashTable) -> None:
    capacity = hash_table.capacity
    new_capacity = capacity * 2
    values = hash_table.values

    hash_table.values = [[] for _ in range(new_capacity)]
    hash_table.capacity = new_capacity

    for hash in range(capacity):
        for key_value in values[hash]:
            if key_value:
                put(hash_table, *key_value)


def create_hash_table() -> HashTable:
    return HashTable()


def delete_hash_table(hash_table: HashTable) -> None:
    for hash in range(hash_table.capacity):
        for _ in range(len(hash_table.values[hash])):
            del hash_table.values[hash][0]


def put(hash_table: HashTable, key: Key, value: Value) -> None:
    if get_load_factor(hash_table) <= 0.8:
        hash = hash_function(key, hash_table.capacity)
        for index, key_value in enumerate(hash_table.values[hash]):
            if key_value[0] == key:
                hash_table.values[hash][index] = (key, value)
                break
        else:
            hash_table.values[hash].append((key, value))
    else:
        resize(hash_table)
        put(hash_table, key, value)

    hash_table.keys_number += 1


def remove(hash_table: HashTable, key: Key) -> Value:
    hash = hash_function(key, hash_table.capacity)
    for index, key_value in enumerate(hash_table.values[hash]):
        if key_value[0] == key:
            value = key_value[1]
            del hash_table.values[hash][index]
            hash_table.keys_number -= 1
            return value
    else:
        raise ValueError("Такого ключа нет в hash table")


def get(hash_table: HashTable, key: Key) -> Value:
    hash = hash_function(key, hash_table.capacity)

    for key_value in hash_table.values[hash]:
        if key_value[0] == key:
            return key_value[1]
    else:
        raise ValueError("Такого ключа нет в hash table")


def has_key(hash_table: HashTable, key: Key) -> bool:
    hash = hash_function(key, hash_table.capacity)

    for key_value in hash_table.values[hash]:
        if key_value[0] == key:
            return True
    return False


def items(hash_table: HashTable) -> list[tuple[Key, Value]]:
    output = []

    for hash in range(hash_table.capacity):
        for key_value in hash_table.values[hash]:
            output.append(key_value)

    return output
