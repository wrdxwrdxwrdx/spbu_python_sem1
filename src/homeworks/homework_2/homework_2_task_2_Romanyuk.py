import csv
from os.path import exists


def create_word_list(file_name):
    word_counter = {}

    with open(file_name, 'r') as file:
        for line in file:
            for word in line.split():
                if word in word_counter.keys():
                    word_counter[word] += 1
                else:
                    word_counter.update({word: 1})

    return word_counter


def write_in_file(write_file, word_counter):
    with open(write_file, 'w') as file:
        writer = csv.writer(file)
        for word in word_counter:
            writer.writerow([word, word_counter[word]])


if __name__ == '__main__':
    read_file = input('input file [src].txt: ')
    write_file = input('output file [dst].csv: ')
    if exists(read_file):
        word_counter = create_word_list(read_file)

        write_in_file(write_file, word_counter)

        print(f'{write_file} done')
    else:
        print(f'{read_file} does not exist')
