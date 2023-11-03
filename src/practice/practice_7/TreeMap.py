from dataclasses import dataclass
from typing import TypeVar, Generic, Optional

V = TypeVar("V")
Key = TypeVar("Key")
Value = TypeVar("Value")


@dataclass
class TreeNode(Generic[V]):
    key: Key
    value: V
    left: Optional["TreeNode[V]"] = None
    right: Optional["TreeNode[V]"] = None


@dataclass
class TreeMap(Generic[V]):
    root: Optional["TreeNode[V]"] = None
    size: int = 0


# err
def create_tree_map() -> TreeMap:
    return TreeMap()


# err
def delete_tree_map(map: TreeMap) -> None:
    def delete_node(node: TreeNode):
        left_node = node.left
        right_node = node.right

        if left_node is None and right_node is None:
            del node

        elif left_node is not None:
            delete_node(node.left)
            del node

        elif right_node is not None:
            delete_node(node.right)
            del node

    if map.root is not None:
        map.root = delete_node(map.root)
        map.size = 0


# err
def put(map: TreeMap, key: Key, value: Value) -> None:
    if map.root is None:
        map.root = TreeNode(key, value)
        map.size += 1

    else:

        def binary_search_put(map: TreeMap, node: TreeNode, key: Key) -> None:
            if node.key == key:
                node.value = value

            elif key < node.key:
                if node.left is None:
                    node.left = TreeNode(key, value)
                    map.size += 1
                else:
                    return binary_search_put(map, node.left, key)

            elif key > node.key:
                if node.right is None:
                    node.right = TreeNode(key, value)
                    map.size += 1
                else:
                    return binary_search_put(map, node.right, key)

        binary_search_put(map, map.root, key)


# err
def get(map: TreeMap, key: Key) -> Value:
    if not has_key(map, key):
        raise ValueError("Элемента нет в дереве")

    def binary_search_get(node: TreeNode, key: Key) -> Value:
        if node.key == key:
            return node.value
        elif key < node.key:
            return binary_search_get(node.left, key)
        else:
            return binary_search_get(node.right, key)

    return binary_search_get(map.root, key)


# err
def has_key(map: TreeMap, key: Key) -> bool:
    def binary_search_has_key(node: TreeNode, key: Key) -> bool:
        if node.key == key:
            return True
        elif key < node.key:
            if node.left is None:
                return False
            else:
                return binary_search_has_key(node.left, key)

        else:
            if node.right is None:
                return False
            else:
                return binary_search_has_key(node.right, key)

    if map.root is None:
        return False
    return binary_search_has_key(map.root, key)


# err
def remove(map: TreeMap, key: Key) -> Value:
    def remove_node(node: TreeNode, key: Key) -> (TreeNode, Value):
        if key < node.key:
            new_left_child, value = remove_node(node.left, key)
            node.left = new_left_child
            return node, value
        elif node.key < key:
            new_right_child, value = remove_node(node.right, key)
            node.right = new_right_child
            return node, value

        if node.left is None and node.right is None:
            return None, node.value
        elif node.left is None and node.right is not None:
            return node.right, node.value
        elif node.left is not None and node.right is None:
            return node.left, node.value
        else:

            def find_min_node(node: TreeNode) -> TreeNode:
                def binary_search(node: TreeNode) -> TreeNode:
                    if node.left is None:
                        return node
                    else:
                        binary_search(node.left)

                return binary_search(node)

            value = node.value

            min_node = find_min_node(node.right)

            remove_node(node, min_node.key)

            node.key = min_node.key
            node.value = min_node.value

            return node, value

    if not has_key(map, key):
        raise ValueError("Элемента нет в дереве")
    if map.size == 1:
        root = map.root

        map.root = None
        map.size -= 1
        return root.value

    map.root, value = remove_node(map.root, key)
    return value


# err
def traverse(map: TreeMap, order: str) -> list[Value]:
    def postorder_comparator(node: TreeNode[V]) -> filter:
        return filter(None, (node.left, node.right, node))

    def inorder_comparator(node: TreeNode[V]) -> filter:
        return filter(None, (node.left, node, node.right))

    def preorder_comparator(node: TreeNode[V]) -> filter:
        return filter(None, (node, node.left, node.right))

    if map.size == 0:
        return []

    order_list = []

    def create_order(node: TreeNode, func) -> None:
        node_order = func(node)

        for i in node_order:
            if i != node:
                create_order(i, func)
            else:
                order_list.append(i.value)

    order = order.lower()

    if order == "preorder":
        create_order(map.root, preorder_comparator)
    elif order == "inorder":
        create_order(map.root, inorder_comparator)
    elif order == "postorder":
        create_order(map.root, postorder_comparator)
    else:
        raise ValueError("Введен неверный порядок")
    return order_list
