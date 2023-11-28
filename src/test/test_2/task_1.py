def fibonacci(n: int) -> int:
    first_number = 0
    second_number = 1
    for i in range(n):
        first_number, second_number = second_number, first_number + second_number

    return first_number


def check_input(user_input: str) -> None:
    try:
        number = float(user_input)
    except ValueError:
        raise ValueError("You entered not number") from None

    if number % 1 != 0:
        raise ValueError("number must be Integer")

    if not (0 <= number <= 90):
        raise ValueError("number must be from 0 to 90")


def main() -> None:
    try:
        user_input = input(
            "Enter number n from 0 to 90. To find n-th number of Fibonacci "
        )
        check_input(user_input)
        result = fibonacci(int(user_input))
        if user_input == "1":
            print(f"{user_input}-st element is {result}")
        elif user_input == "2":
            print(f"{user_input}-nd element is {result}")
        elif user_input == "3":
            print(f"{user_input}-rd element is {result}")
        else:
            print(f"{user_input}-th element is {result}")

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
