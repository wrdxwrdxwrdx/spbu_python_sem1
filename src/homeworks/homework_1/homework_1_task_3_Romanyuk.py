from sys import argv
from os.path import exists


def wc(prefix, file_name):
    line_counter = 0
    word_counter = 0
    char_counter = 0
    byte_counter = 0

    with open(file_name, 'r') as file:
        for line in file.readlines():
            word_counter += len(line.split())
            encoded_bytes = line.encode("utf-8")
            byte_counter += len(encoded_bytes)

            for char in line:
                char_counter += 1
                if char == '\n':
                    line_counter += 1

    if prefix == '-l':
        print(f'{line_counter} {file_name}')
    elif prefix == '-m':
        print(f'{char_counter} {file_name}')
    elif prefix == '-c':
        print(f'{byte_counter} {file_name}')
    elif prefix == '-w':
        print(f'{word_counter} {file_name}')
    elif prefix == '-all':
        print(f'{line_counter} {word_counter} {byte_counter} {file_name}')
    else:
        print('ошибка в написании параметра')


def head(prefix, file_name, line_number):
    with open(file_name, 'r') as file:
        if prefix == '-n':
            for _ in range(line_number):
                print(file.readline())

        elif prefix == '-c':
            line = file.readline()

            while line_number >= len(line.encode("utf-8")):
                print(line.replace('\n', ''))
                line_number -= len(line.encode("utf-8"))
                line = file.readline()

            line = line.encode('utf-8')[:line_number]
            print(line.decode('utf-8'))


def tail(prefix, file_name, line_number):
    with open(file_name, 'r') as file:

        # print lines

        if prefix == '-n':
            file_lines = file.readlines()
            for i in range(len(file_lines) - line_number, len(file_lines)):
                print(file_lines[i].strip())

        # print bytes

        elif prefix == '-c':
            file_lines = file.readlines()
            output_lines = []
            line = file_lines.pop(-1)
            while line_number >= len(line.encode('utf-8')):
                line_number -= len(line.encode('utf-8'))
                output_lines.append(line)
                line = file_lines.pop(-1)

            output_lines.append(line.encode('utf-8')[len(line.encode('utf-8')) - line_number:].decode('utf-8'))

            for lines in output_lines[::-1]:
                print(lines.replace('\n', ''))


if __name__ == "__main__":
    line_number = 10
    prefix = '-all'

    is_running = True

    if len(argv[1:]) == 3:
        function, prefix, file_name = argv[1:]

    elif len(argv[1:]) == 2:
        function, file_name = argv[1:]

    elif len(argv[1:]) == 4:
        function, prefix, line_number, file_name = argv[1:]
        line_number = int(line_number)
    else:
        function = None
        is_running = False
        print("Введите корректную команду")


    if is_running and exists(file_name):
        if function == "wc":
            wc(prefix, file_name)
        elif function == 'head':
            head(prefix, file_name, line_number)
        elif function == 'tail':
            tail(prefix, file_name, line_number)
        else:
            print('Введена неверныая команда')
    elif is_running:
        print(f'{file_name} Нет такого файла')
