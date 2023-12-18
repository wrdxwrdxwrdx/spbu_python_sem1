from os.path import exists

from src.homeworks.homework_6.AVL_Tree import *


def format_address(address: str) -> list[str, int, int]:
    address_arr = address.split()
    address_arr[1], address_arr[2] = int(address_arr[1]), int(address_arr[2])
    return address_arr


def create_address(storage: TreeMap, address: str, index: int) -> None:
    put(storage, format_address(address), index)


def get_index(storage: TreeMap, address: str) -> str:
    return get(storage, format_address(address))


def rename_street(storage: TreeMap, street: str, new_name: str) -> None:
    for previous_name in getAll(
        storage, [street, 0, 0], [street, float("inf"), float("inf")]
    ):
        house, building = previous_name[1:]
        put(storage, [new_name, house, building], remove(storage, previous_name))


def delete_block(storage: TreeMap, address: str) -> None:
    remove(storage, format_address(address))


def delete_house(storage: TreeMap, street: str, house: str) -> None:
    for address in getAll(
        storage, [street, int(house)], [street, int(house), float("inf")]
    ):
        remove(storage, address)


def delete_street(storage: TreeMap, street: str) -> None:
    for address in getAll(
        storage, [street, 0, 0], [street, float("inf"), float("inf")]
    ):
        remove(storage, address)


def list_command(storage: TreeMap, address_1: str, address_2: str) -> list[str]:
    address_arr = list_function(
        storage, format_address(address_1), format_address(address_2)
    )
    address_arr.sort()
    address_arr = list(map(lambda x: f"{x[0]} {x[1]} {x[2]}", address_arr))
    return address_arr


def detect_command(storage: TreeMap, line: str) -> Optional[str]:
    """detect command and use it"""
    attributes = line.split()
    command = attributes.pop(0)
    try:
        if command == "CREATE":
            create_address(storage, " ".join(attributes[:-1]), int(attributes[-1]))
        elif command == "GET":
            try:
                return str(get_index(storage, " ".join(attributes))) + "\n"
            except:
                return "None\n"

        elif command == "RENAME":
            street_name = attributes[0]
            new_street_name = attributes[1]
            rename_street(storage, street_name, new_street_name)
        elif command == "DELETE_BLOCK":
            delete_block(storage, " ".join(attributes))
        elif command == "DELETE_HOUSE":
            delete_house(storage, *attributes)
        elif command == "DELETE_STREET":
            delete_street(storage, *attributes)
        elif command == "LIST":
            address_1 = " ".join(attributes[:3])
            address_2 = " ".join(attributes[3:])
            list_arr = list_command(storage, address_1, address_2)
            if list_arr:
                list_str = "\n".join(list_arr) + "\n\n"
            else:
                list_str = "\n"
            return list_str

    except ValueError as err:
        pass
    return


def static_mode(storage: TreeMap, input_file: str, output_file: str) -> None:
    with open(output_file, "w") as output_file:
        with open(input_file, "r") as input_file:
            input_file.readline()
            for command in input_file.readlines():
                command = command.strip()
                line = detect_command(storage, command)
                if line is not None:
                    output_file.write(line)


def interactive_mode(storage):
    print("To exit from interactive_mode print EXIT. Enter command: ")
    command = ""
    while command != "EXIT":
        command = input()
        try:
            result = detect_command(storage, command)
            if result:
                print(result)

        except Exception as error:
            print(error)


def chose_mode(storage: TreeMap):
    user_input = input(
        "Chose mode:\n" "    1) interactive_mode\n" "    2) static_mode\n"
    )
    if user_input == "1":
        interactive_mode(storage)
    elif user_input == "2":
        input_file = input("Enter input_file: ")
        output_file = input("Enter output_file: ")

        if not exists(input_file):
            raise ValueError(f"file {input_file} does not exist")

        static_mode(storage, input_file, output_file)
    else:
        raise ValueError(f"You need to enter 1 or 2, not {user_input}")


def main():
    storage = create_tree_map()
    try:
        chose_mode(storage)
    except Exception as error:
        print(error)
        main()


if __name__ == "__main__":
    main()
