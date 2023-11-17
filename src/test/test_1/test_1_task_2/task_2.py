from deque import *


def main() -> None:
    try:
        deque = create_deque()

        print(f"is_empty: {is_empty(deque)}")

        for value in range(5, 0, -1):
            pushFront(deque, value)

        for value in range(5, 10):
            pushBack(deque, value)

        display(deque)

        print(f"\npopBack: {popBack(deque)}")

        display(deque)

        print(f"\npopFront: {popFront(deque)}")

        display(deque)

        print(f"\ndeque size: {size(deque)}")

        for i in range(10):
            print(f"\npopFront: {popFront(deque)}")
            display(deque)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
