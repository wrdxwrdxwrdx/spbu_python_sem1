from sys import argv
from os.path import exists


def get_array(file_name):
    with open(file_name, "r") as file:
        arr = list(map(int, file.readline().split()))
    return arr


def sort_arr(a, b, arr):
    less_a = []
    in_ab = []
    more_b = []
    for i in arr:
        if i < a:
            less_a.append(i)
        elif i > b:
            more_b.append(i)
        else:
            in_ab.append(i)
    return less_a, in_ab, more_b


def write_file(file_name, less_a, in_ab, more_b):
    with open(file_name, "w") as write_file:
        write_file.write(" ".join(map(str, less_a)) + "\n")
        write_file.write(" ".join(map(str, in_ab)) + "\n")
        write_file.write(" ".join(map(str, more_b)) + "\n")
    return True


def file_check(read_file_name, write_file_name):
    if not (exists(read_file_name)):
        print(f"не существует {read_file_name}")
        return False
    if exists(write_file_name):
        print(f"файл {write_file_name} уже существует")
        return False
    return True


def main():
    a, b, read_file_name, write_file_name = argv[1:]
    a, b = int(a), int(b)
    if file_check(read_file_name, write_file_name):
        arr = get_array(read_file_name)
        less_a, in_ab, more_b = sort_arr(a, b, arr)
        write_file(write_file_name, less_a, in_ab, more_b)


if __name__ == "__main__":
    main()
