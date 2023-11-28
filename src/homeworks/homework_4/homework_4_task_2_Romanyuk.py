def whole_part_binary(number):
    number = abs(number)

    whole_part = int(number)
    output = []

    while whole_part:
        output.append(whole_part % 2)
        whole_part //= 2

    output = output[::-1]
    output.append(".")

    return output


def decimal_part_binary(number):
    output = []

    decimal_part = number % 1

    if decimal_part != 0:
        while decimal_part != 0:
            decimal_part *= 2
            output.append(int(decimal_part))
            if int(decimal_part):
                decimal_part = decimal_part % 1

    return output


def denary_to_binary(number):
    is_minus = number < 0

    output = whole_part_binary(number) + decimal_part_binary(number)

    if is_minus:
        return "-" + "".join(map(str, output))
    return "+" + "".join(map(str, output))


def count_shifted_order(q, k):
    return q + 2 ** (k - 1) - 1


def floating_point_number(number, mantissa_bit, exponent_bit):
    bin_number = denary_to_binary(number)

    if bin_number[1] == ".":
        q = 1 - bin_number.find("1")
        bin_number = bin_number.replace(".", "")
        mantissa = bin_number[bin_number.index("1") + 1 :]

    else:
        q = bin_number.find(".") - 2
        bin_number = bin_number.replace(".", "")
        mantissa = bin_number[2:]

    mantissa = mantissa.ljust(mantissa_bit, "0")
    exponent = denary_to_binary(count_shifted_order(q, exponent_bit))[1:-1]

    sign = int(bin_number[0] == "-")

    return f"{sign} {exponent} {mantissa}"


def binary_exponent(number):
    if number[1] == ".":
        q = 2 - number.find("1")
        mantissa = number[0] + "0." + number[number.find("1") :]
    else:
        q = number.find(".") - 1
        number = number.replace(".", "")
        mantissa = number[0] + "0." + number[1:]

    return f"{mantissa[:27]} * {2}^{q}"


def main():
    number = float(input("число: "))

    print(f"экспоненциальная запись числа: {binary_exponent(denary_to_binary(number))}")
    print("Выберите формат записи числа")

    choice = int(input("1) FP64\n" "2) FP32\n" "3) FP16\n"))

    if choice == 1:
        print((f"число в FP64: {floating_point_number(number, 52, 11)}"))
    elif choice == 2:
        print(f"число в FP32: {floating_point_number(number, 23, 8)}")
    else:
        print(f"число в FP16: {floating_point_number(number, 10, 5)}")


if __name__ == "__main__":
    main()
