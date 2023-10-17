def denary_to_binary(number, accuracy=10):
    is_minus = number < 0
    number = abs(number)
    decimal_part = number % 1
    whole_part = int(number)
    res = []
    while whole_part:
        res.append(whole_part % 2)
        whole_part //= 2
    res = res[::-1]
    res.append(".")

    if decimal_part != 0:
        for i in range(accuracy - len(res)):
            decimal_part *= 2
            res.append(int(decimal_part))
            if int(decimal_part):
                decimal_part = decimal_part % 1

    if is_minus:
        return "-" + "".join(map(str, res))
    return "+" + "".join(map(str, res))


def count_shifted_order(q, k):
    return q + 2 ** (k - 1) - 1


def double_number(number, mantissa_bit, exponent_bit):
    bin_number = denary_to_binary(number, mantissa_bit + 2)
    q = bin_number.index(".") - 2
    exponent = denary_to_binary(count_shifted_order(q, exponent_bit))[1:-1]
    sign = int(bin_number[0] == "-")
    mantissa = (
        bin_number[2 : bin_number.index(".")] + bin_number[bin_number.index(".") + 1 :]
    )

    return f"{sign} {exponent} {mantissa}"


def denary_exponent(number):
    p = 10
    q = 0
    while abs(number) >= 1:
        q += 1
        number /= 10
    return f"{number} * {p}^{q}"


def main(choice, number):
    print(f"экспоненциальная запись числа: {denary_exponent(number)}")
    if choice == 1:
        print((f"число в FP64: {double_number(number, 52, 11)}"))
    elif choice == 2:
        print(f"число в FP32: {double_number(number, 23, 8)}")
    else:
        print(f"число в FP16: {double_number(number, 10, 5)}")


if __name__ == "__main__":
    number = float(input("число: "))
    print("Выберите формат записи числа")
    choice = int(input("1) FP64\n" "2) FP32\n" "3) FP16\n"))

    main(choice, number)
