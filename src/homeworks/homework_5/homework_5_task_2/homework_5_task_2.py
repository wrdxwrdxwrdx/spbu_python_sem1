from dna_functions import decode, encode

INPUT_TEXT = "Выберите функцию над днк:\n" "1) encode\n" "2) decode\n"
ENCODE_TEXT = "Введите днк: "
DECODE_TEXT = "Введите код днк: "


def main() -> None:
    try:
        function_number = input(INPUT_TEXT)

        if function_number == "1":
            dna = input(ENCODE_TEXT)
            print(f"Код днк: {encode(dna)}")
        elif function_number == "2":
            dna_code = input(DECODE_TEXT)
            print(f"днк: {decode(dna_code)}")
        else:
            raise ValueError("Введен несуществующий номер функции")

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
