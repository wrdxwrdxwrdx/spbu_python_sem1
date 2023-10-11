from list import *

if __name__ == "__main__":
    ls = create()
    insert(ls, 0, 0)
    insert(ls, 1, 1)
    insert(ls, 2, 2)
    insert(ls, 3, 3)
    print(head(ls))
    print(tail(ls))
    print(retrieve(ls, 3))
    delete(ls, 0)
    print(head(ls))
