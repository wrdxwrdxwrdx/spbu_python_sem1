def array_shift(array, m):
    array = array[::-1]
    n = len(array) - m
    array[:n] = array[n - 1 :: -1]
    array[n:] = array[len(array) : n - 1 : -1]

    return array


if __name__ == "__main__":
    input_array = input("Введите массив через пробел: ")
    array = list(map(int, input_array.split()))
    m = int(input("Введите число m: "))
    print(f"Результат: {array_shift(array, m)}")
