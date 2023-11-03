from TreeMap import *


def main():
    try:
        m = create_tree_map()
        put(m, 8, 8)
        put(m, 3, 3)
        put(m, 1, 1)
        put(m, 6, 6)
        put(m, 4, 4)
        put(m, 7, 7)
        put(m, 10, 10)
        put(m, 14, 14)
        put(m, 13, 13)

        print(traverse(m, "inorder"))
        print(remove(m, 6))

        get(m, 8)

        print(traverse(m, "inorder"))

        print(has_key(m, 8))

        delete_tree_map(m)

        print(traverse(m, "preorder"))
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
