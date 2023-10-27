from list import *


def check_insert(function_result):
    if not function_result:
        print("не удалось добавить элемент")


def check_locate(function_result):
    if not function_result:
        print("данного элемента нет в списке")
    else:
        print(f"заданный элемент стоит на позиции: {function_result}")


def check_delete(function_result):
    if not function_result:
        print("не удалось удалить элемент")


def check_retrieve(function_result):
    if not function_result:
        print("не удалось найти элемент")
    else:
        print(f"на заданной позиции стоит: {function_result}")


def main():
    try:
        ls = create()
        check_retrieve(retrieve(ls, -1))

        check_insert(insert(ls, 0, 0))
        check_insert(insert(ls, 1, 1))
        check_insert(insert(ls, 2, 2))
        check_insert(insert(ls, 3, 3))
        check_insert(insert(ls, 10, 3))

        print(f"первый элемент: {head(ls)}")
        print(f"второй элемент: {tail(ls)}")

        check_retrieve(retrieve(ls, 3))

        check_delete(delete(ls, 0))
        check_delete(delete(ls, 100))

        check_locate(locate(ls, 4))
        check_locate(locate(ls, 3))

        print(f"первый элемент: {head(ls)}")
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
