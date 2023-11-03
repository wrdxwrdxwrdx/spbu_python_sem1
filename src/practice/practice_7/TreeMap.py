from dataclasses import dataclass
from typing import TypeVar, Generic

V = TypeVar("V")
Key = TypeVar("Key")
Value = TypeVar("Value")


@dataclass
class TreeNode(Generic[V]):
    key: Key
    value: V
    left: "TreeNode[V]" = None
    right: "TreeNode[V]" = None


@dataclass
class TreeMap(Generic[V]):
    root: TreeNode[V] | None = None
    size: int = 0


# err
def create_tree_map() -> TreeMap:
    return TreeMap()


# err
def delete_tree_map(map: TreeMap):
    map.root = None
    map.size = 0


# err
def put(map: TreeMap, key: Key, value: Value):
    if map.root is None:
        map.root = TreeNode(key, value)
        map.size += 1

    else:

        def binary_search_put(map: TreeMap, node: TreeNode, key: Key):
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
    def binary_search_get(node: TreeNode, key: Key) -> Value:
        if node.key == key:
            return node.value
        elif key < node.key:
            if node.left is None:
                raise ValueError("Элемента нет в дереве")
            else:
                return binary_search_get(node.left, key)
        else:
            if node.right is None:
                raise ValueError("Элемента нет в дереве")
            else:
                return binary_search_get(node.right, key)

    if map.root is None:
        raise ValueError("Элемента нет в дереве")
    return binary_search_get(map.root, key)


# err
def has_key(map: TreeMap, key: Key) -> bool:
    def binary_search_has_key(node: TreeNode, key: Key):
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
    remove_value = get(map, key)

    def binary_search_remove(node: TreeNode, key: Key) -> TreeNode | None:
        if node is None:
            return None

        if node.key == key:
            if node.left is None and node.right is None:
                return None
            if node.left is not None and node.right is None:
                return node.left
            if node.left is None and node.right is not None:
                return node.right

            right_branch = node.right
            while right_branch.left:
                right_branch = right_branch.left
            node.value = right_branch.value
            node.key = right_branch.key
            node.right = binary_search_remove(node.right, node.key)

        elif node.left is None and node.right is None:
            raise ValueError("Элемента нет в дереве")

        elif node.key > key:
            node.left = binary_search_remove(node.left, key)
        else:
            node.right = binary_search_remove(node.right, key)
        return node

    if map.root is None:
        raise ValueError("Элемента нет в дереве")
    else:
        binary_search_remove(map.root, key)
    map.size -= 1
    return remove_value


# err
def traverse(map: TreeMap, order: str) -> list[Value]:
    def inorder(node: TreeNode) -> list[Value]:
        if node.left and node.right:
            return [node.value] + inorder(node.left) + inorder(node.right)
        elif node.left:
            return [node.value] + inorder(node.left)
        elif node.right:
            return [node.value] + inorder(node.right)
        else:
            return [node.value]

    def postorder(node: TreeNode, array: list = []) -> list[Value]:
        if node.left:
            postorder(node.left, array)
        array.append(node.value)
        if node.right:
            postorder(node.right, array)

        return array

    def preorder(node: TreeNode) -> list[Value]:
        def direct_order_right(node: TreeNode):
            if node.left and node.right:
                return (
                    [node.value]
                    + direct_order_right(node.right)
                    + direct_order_right(node.left)
                )
            if node.right:
                return [node.value] + direct_order_right(node.right)
            elif node.left:
                return [node.value] + direct_order_right(node.left)
            else:
                return [node.value]

        return direct_order_right(node)[::-1]

    order = order.lower()

    if map.root is None and order in ("inorder", "postorder", "preorder"):
        return []

    if order == "inorder":
        return inorder(map.root)
    if order == "postorder":
        return postorder(map.root)
    if order == "preorder":
        return preorder(map.root)
    else:
        raise ValueError("Указан неверный порядок")
