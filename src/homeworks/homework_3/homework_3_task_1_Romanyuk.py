def curry_explict(function, arity):
    if arity < 0:
        raise ValueError("введена арность меньше 0")

    def main_curry_function(args):
        if len(args) == arity:
            if arity == 0:
                return function
            try:
                return function(*args)
            except TypeError:
                raise ValueError("введена неверная арность(curry_explict)")

        return lambda new_argument: main_curry_function([*args, new_argument])

    return main_curry_function([])


def uncurry_explicit(function, arity):
    def main_uncurry_function(*args):
        try:
            if len(args) == 0:
                return function()
            function_return = function(args[0])

            for i in range(1, len(args)):
                function_return = function_return(args[i])

            return function_return

        except TypeError:
            raise ValueError("введена неверная арность(uncurry_explicit)")

    return main_uncurry_function
