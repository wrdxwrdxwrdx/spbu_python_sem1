def curry_explict(function, arity):
    if arity < 0:
        return False

    def main_curry_function(args):
        if len(args) == arity:
            if arity == 0:
                return function
            try:
                return function(*args)
            except TypeError:
                print("введена неверная арность(curry_explict)")

        def curry(new_argument):
            return main_curry_function([*args, new_argument])

        return curry

    return main_curry_function([])


def uncurry_explicit(function, arity):
    def main_uncurry_function(*args):
        if len(args) != arity:
            print("введена неверная арность(uncurry_explicit)")
            return
        elif len(args) == 0:
            return function()
        f = function(args[0])

        for i in range(1, len(args)):
            f = f(args[i])

    return main_uncurry_function


def get_user_input():
    user_function = eval(input("Введите функцию: "))
    arity = int(input("Введите арность функции: "))
    curry_user_function = curry_explict(user_function, arity)
    uncurry_user_function = uncurry_explicit(curry_user_function, arity)
    return curry_user_function, uncurry_user_function


if __name__ == "__main__":
    curry_user_function, uncurry_user_function = get_user_input()
    if curry_user_function:
        print(
            "\nкаррированая функция curry_user_function\n"
            "декаррированая функция uncurry_user_function\n"
        )
        while True:
            eval(input("Введите название функции и ее параметры: "))
    else:
        print("Введена арность меньше 0")
