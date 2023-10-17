from queue import *

if __name__ == "__main__":
    queue = create_queue()

    print(f"is_null: {is_null(queue)}")

    for i in range(10):
        enqueue(queue, i)

    print(f"is_full: {is_full(queue)}")
    print(f"peek: {peek(queue)}")

    dequeue(queue)

    print(f"is_full: {is_full(queue)}")
    print(f"peek: {peek(queue)}")