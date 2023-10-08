from os.path import exists


def delete(dna, start, end):
    start_index = dna.find(start)
    end_index = dna.find(end, start_index)

    return dna[:start_index] + dna[end_index + len(end) :]


def insert(dna, start, fragment):
    start_index = dna.find(start)

    return dna[: start_index + len(start)] + fragment + dna[start_index + len(start) :]


def replace(dna, template, fragment):
    return dna.replace(template, fragment, 1)


def write_array(array, write_file_name):
    with open(write_file_name, "w") as write_file:
        write_file.write("\n".join(dna_array))


def generate_dna(read_file_name):
    dna_array = []

    with open(read_file_name, "r") as read_file:
        input_array = [read_file.readline().strip() for _ in range(3)]
        length_dna, dna, command_number = (
            int(input_array[0]),
            input_array[1],
            int(input_array[2]),
        )

        for i in range(command_number):
            line = read_file.readline().split()
            if line[0] == "DELETE":
                dna = delete(dna, line[1], line[2])
            elif line[0] == "INSERT":
                dna = insert(dna, line[1], line[2])
            elif line[0] == "REPLACE":
                dna = replace(dna, line[1], line[2])
            dna_array.append(dna)
    return dna_array


if __name__ == "__main__":
    read_file_name = input("file with commands [src].txt: ")
    write_file_name = input("output file [dst].txt: ")

    if exists(read_file_name):
        dna_array = generate_dna(read_file_name)
        write_array(dna_array, write_file_name)
        print(f"{write_file_name} done")
    else:
        print(f"{read_file_name} does not exist")
