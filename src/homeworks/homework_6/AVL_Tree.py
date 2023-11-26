from dataclasses import dataclass
from typing import TypeVar, Generic, Optional

Key = TypeVar("Key")
Value = TypeVar("Value")


@dataclass
class TreeNode(Generic[Value]):
    key: Key
    value: Value
    left: Optional["TreeNode[Value]"] = None
    right: Optional["TreeNode[Value]"] = None
    height: int = 1


@dataclass
class TreeMap(Generic[Value]):
    root: Optional["TreeNode[Value]"] = None
    size: int = 0


# AVL-TREE FUNCTIONS


def correct_height(root) -> None:
    """Set height for root by children height"""
    root.height = max(get_root_height(root.right), get_root_height(root.left)) + 1


def set_height(root: TreeNode) -> int:
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    root.height = max(set_height(root.left), set_height(root.right)) + 1
    return root.height


def get_balance_factor(root: TreeNode) -> int:
    """Count balance factor for root"""
    if root is None:
        return 0
    return get_root_height(root.left) - get_root_height(root.right)


def get_root_height(root: TreeNode) -> int:
    """
    Return height of the root\n
    if root is None -> 0
    """
    if root is None:
        return 0
    return root.height


def left_rotate(root: TreeNode) -> TreeNode:
    """Perform left rotation for root"""
    new_root = root.right
    root.right = new_root.left
    new_root.left = root
    correct_height(root)
    correct_height(new_root)
    return new_root


def right_rotate(root: TreeNode) -> TreeNode:
    """Perform right rotation for root"""
    new_root = root.left
    root.left = new_root.right
    new_root.right = root
    correct_height(root)
    correct_height(new_root)
    return new_root


def balance_node(root: TreeNode) -> TreeNode:
    """Balance node using AVL_tree rule"""

    if root is None:
        return None

    correct_height(root)

    if get_balance_factor(root) >= 2:
        if get_balance_factor(root.left) < 0:
            root.left = left_rotate(root.left)
        return right_rotate(root)

    elif get_balance_factor(root) <= -2:
        if get_balance_factor(root.right) > 0:
            root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def remove_node(root: TreeNode, key: Key) -> (Optional[TreeNode], Value):
    """Remove key from root"""

    def find_min(root: TreeNode) -> TreeNode:
        """Return root with minimal key under specified root"""
        root_copy = root
        while root_copy.left:
            root_copy = root_copy.left
        return root_copy

    if root.left is None and root.right is None:
        if key == root.key:
            return None, root.value
        else:
            raise ValueError(f"there is no key {key} in the tree")

    if key == root.key:
        value = root.value
        if root.right is None:
            return root.left, value
        if root.left is None:
            return root.right, value

        root_min_key = find_min(root.right)
        new_root = TreeNode(key=root_min_key.key, value=root_min_key.value)
        new_root.left = root.left
        new_root.right = remove_node(root.right, new_root.key)[0]
        return balance_node(new_root), value

    if key < root.key:
        if root.left is None:
            raise ValueError(f"there is no key {key} in the tree")

        root.left, value = remove_node(root.left, key)
    else:
        if root.right is None:
            raise ValueError(f"there is no key {key} in the tree")
        root.right, value = remove_node(root.right, key)
    return balance_node(root), value


def traverse(tree_map: TreeMap) -> list[(Key, Value)]:
    """Return a list with keys and values from AVL_tree"""

    def traverse_node(root: TreeNode) -> list[(Key, Value)]:
        """Return a list with keys and values from node"""

        if root is None:
            return []
        key_arr = [(root.key, root.value)]
        key_arr += traverse_node(root.left) + traverse_node(root.right)
        return key_arr

    return traverse_node(tree_map.root)


# MAIN FUNCTIONS


def create_tree_map() -> TreeMap:
    """Create new TreeMap object"""
    return TreeMap()


def get(tree_map: TreeMap, key: Key) -> Value:
    """Return value of key in AVL_tree"""

    def search_key(root: TreeNode, key: Key) -> Value:
        """Search for key in AVl_tree and return value"""
        if root is None:
            raise ValueError(f"there is no key {key} in the tree")

        if key == root.key:
            return root.value
        elif key < root.key:
            return search_key(root.left, key)
        else:
            return search_key(root.right, key)

    return search_key(tree_map.root, key)


def has_key(tree_map: TreeMap, key: Key) -> bool:
    """Return is there a key in the tree"""

    def check_key(root: TreeNode, key: Key) -> bool:
        """Search for key in AVl_tree"""

        if root is None:
            return False

        if key == root.key:
            return True
        elif key < root.key:
            return check_key(root.left, key)
        else:
            return check_key(root.right, key)

    return check_key(tree_map.root, key)


def get_minimum(tree_map: TreeMap) -> Key:
    """Return minimal key in AVL_tree"""
    if tree_map.root is None:
        raise ValueError("Tree is empty")

    root_copy = tree_map.root
    while root_copy.left:
        root_copy = root_copy.left
    return root_copy.key


def get_maximum(tree_map: TreeMap) -> Key:
    """Return maximal key in AVL_tree"""
    if tree_map.root is None:
        raise ValueError("Tree is empty")

    root_copy = tree_map.root
    while root_copy.right:
        root_copy = root_copy.right
    return root_copy.key


def get_upper_bound(tree_map: TreeMap, key: Key) -> Key:
    """Return the smallest key in the structure,
    which is strictly greater than the specified key"""
    max_key = get_maximum(tree_map)

    if max_key <= key:
        raise ValueError(f"No one key is strictly greater than {key}")

    def search_key(root: TreeNode, upper_bound: Key) -> Key:
        """Search for key in AVl_tree which is strictly greater than the specified key"""
        if key < root.key and root.left is not None:
            return search_key(root.left, min(root.key, upper_bound))

        elif key > root.key and root.right is not None:
            return search_key(root.right, upper_bound)

        if root.key > key:
            return root.key
        return upper_bound

    return search_key(tree_map.root, max_key)


def get_lower_bound(tree_map: TreeMap, key: Key) -> Key:
    """Returns the smallest key in the structure,
    which is greater than or equal to the specified key"""
    max_key = get_maximum(tree_map)

    if max_key < key:
        raise ValueError(f"No one key is greater than or equal to {key}")

    def search_key(root: TreeNode, lower_bound: Key) -> Key:
        """Search for key in AVl_tree which is greater than or equal to the specified key"""
        if key < root.key and root.left is not None:
            return search_key(root.left, min(root.key, lower_bound))

        elif key > root.key and root.right is not None:
            return search_key(root.right, lower_bound)

        if root.key >= key:
            return root.key
        return lower_bound

    return search_key(tree_map.root, max_key)


def put(tree_map: TreeMap, key: Key, value: Value) -> None:
    """Put key_value in AVL_tree"""

    def insert(tree_map: TreeMap, root: TreeNode, key: Key, value: Value) -> TreeNode:
        """Find place for key and balance AVL_tree."""

        if root is None:
            tree_map.size += 1
            return TreeNode(key, value)
        if key == root.key:
            root.value = value
            return root

        if key < root.key:
            root.left = insert(tree_map, root.left, key, value)

        else:
            root.right = insert(tree_map, root.right, key, value)

        return balance_node(root)

    tree_map.root = insert(tree_map, tree_map.root, key, value)


def remove(tree_map: TreeMap, key: Key) -> Value:
    """Remove key from AVL_tree"""

    tree_map.root, value = remove_node(tree_map.root, key)
    tree_map.size -= 1
    return value


def remove_keys(tree_map: TreeMap, left: Key, right: Key) -> None:
    """Delete keys in the specified range from AVL_tree"""

    def remove_keys_node(root: TreeNode, left: Key, right: Key) -> Optional[TreeNode]:
        """Delete keys in the specified range from node"""

        if root:
            root.left = remove_keys_node(root.left, left, right)
            root.right = remove_keys_node(root.right, left, right)

        if root is None:
            return None

        if not (left <= root.key <= right):
            root, value = remove_node(root, root.key)

        return root

    tree_map.root = balance_node(remove_keys_node(tree_map.root, left, right))


def getAll(tree_map: TreeMap, left: Key, right: Key) -> list[Key]:
    """Return a list with keys in the specified range from AVL_tree"""

    def getALL_node(root: TreeNode, left: Key, right: Key) -> list[Key]:
        """Return a list with keys in the specified range from node"""
        if root is None:
            return []
        if left <= root.key <= right:
            key_arr = [root.key]
        else:
            key_arr = []
        key_arr += getALL_node(root.left, left, right) + getALL_node(
            root.right, left, right
        )
        return key_arr

    return getALL_node(tree_map.root, left, right)


def split(tree_map: TreeMap, key: Key) -> tuple[TreeMap, TreeMap]:
    """Splits data by key, returns a pair of two trees. In the first tree,
    all elements are less than key, in the second they are greater than or equal to"""
    small_tree, big_tree = create_tree_map(), create_tree_map()

    key_value_arr = traverse(tree_map)

    for key_value in key_value_arr:
        if key_value[0] < key:
            put(small_tree, *key_value)
        else:
            put(big_tree, *key_value)

    return (small_tree, big_tree)


def join(tree_map: TreeMap, another: TreeMap) -> TreeMap:
    main_min_key = get_minimum(tree_map)
    main_max_key = get_maximum(tree_map)
    another_min_key = get_minimum(another)
    another_max_key = get_maximum(another)

    main_key_number = tree_map.size
    another_key_number = another.size

    # по def распихать
    if another_max_key < main_min_key:
        root_copy = tree_map.root
        while root_copy.left:
            root_copy = root_copy.left
        root_copy.left = another.root
        set_height(tree_map.root)
        tree_map.root = balance_node(tree_map.root)
        return tree_map

    if main_max_key < another_min_key:
        root_copy = another.root
        while root_copy.left:
            root_copy = root_copy.left
        root_copy.left = tree_map.root
        set_height(another.root)
        another.root = balance_node(another.root)
        return another

    if main_key_number < another_key_number:
        for key_value in traverse(tree_map):
            put(another, *key_value)
        return another

    else:
        for key_value in traverse(another):
            put(tree_map, *key_value)
        return tree_map


def list_function(
    tree_map: TreeMap, left: list[str, int, int], right: list[str, int, int]
) -> list[list[str, int, int]]:
    """Return a list with keys in the specified range and list rule from AVL_tree"""

    def list_function_node(
        root: TreeNode, left: list[str, int, int], right: list[str, int, int]
    ) -> list[list[str, int, int]]:
        """Return a list with keys in the specified range and list rule from node"""

        if root is None:
            return []
        if left <= root.key < right:
            key_arr = [root.key]
        else:
            key_arr = []
        key_arr += list_function_node(root.left, left, right) + list_function_node(
            root.right, left, right
        )
        return key_arr

    return list_function_node(tree_map.root, left, right)
