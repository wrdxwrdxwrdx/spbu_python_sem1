from inspect import signature


def curry_explicit(function, arity):
    if len(signature(function).parameters) != arity:
        raise ValueError("введена неверная арность(curry_explict)")

    def main_curry_function(args):
        if len(args) == arity:
            if arity == 0:
                return function
            return function(*args)

        def curry(new_argument):
            return main_curry_function([*args, new_argument])

        return curry

    return main_curry_function([])


def uncurry_explicit(function, arity):
    def main_uncurry_function(*args):
        if len(args) == 0:
            return function()

        function_return = function(args[0])

        try:
            for i in range(1, len(args)):
                function_return = function_return(args[i])
            return function_return

        except TypeError:
            raise ValueError("введена неверная арность(uncurry_explicit)")

    return main_uncurry_function
