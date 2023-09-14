def calculate(x):
    # x**4 + x**3 + x**2 + x + 1 = (x**2 + x)(x**2 + 1) + 1:
    square_x = x ** 2
    return (square_x + x) * (square_x + 1) + 1


if __name__ == "__main__":
    x = int(input("Введите х: "))
    print(f"{x}^4 + {x}^3 + {x}^2 + {x} + 1 = {calculate(x)}")