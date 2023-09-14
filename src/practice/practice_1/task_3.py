def prime(x):
    array = []
    for i in range(2, x+1):
        for q in range(2, int(i**0.5)+1):
            if i % q == 0:
                break
        else:
            array.append(i)
    return array


if __name__ == '__main__':
    x = int(input("Введите число: "))
    result = ', '.join(map(str, prime(x)))
    print(f'Все простые числа не больше {x}: {result}')