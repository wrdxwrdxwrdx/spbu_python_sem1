def get_fractions(max_denominator):
    answer = []
    for denominator in range(2, max_denominator + 1):
        for numerator in range(1, denominator):
            if numerator == 1:
                answer.append((numerator, denominator))

            elif denominator % numerator != 0:
                answer.append((numerator, denominator))

    answer.sort(key=lambda fraction: fraction[0] / fraction[1])
    return answer


def output_fractions(array):
    answer = ""
    for fraction in array:
        answer += f"{fraction[0]}/{fraction[1]}, "
    return answer[:-2]


if __name__ == "__main__":
    max_denominator = int(input("Напишите максимальный знаменатель: "))
    all_fractions = get_fractions(max_denominator)
    print(output_fractions(all_fractions))
