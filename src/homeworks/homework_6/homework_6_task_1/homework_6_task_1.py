from AVL_Tree import *

OUTPUT_FILE = "output_logs.txt"
STORAGE_FILE = "shop_logs.txt"


def add_to_storage(storage: TreeMap, size: int, count: int) -> int:
    """Add to the storage "COUNT" instances of clothing size "SIZE" """
    if has_key(storage, size):
        instances = count + get(storage, size)
        put(storage, size, instances)
    else:
        put(storage, size, count)
    return size


def get_from_storage(storage: TreeMap, size: int) -> int:
    """find out the number of copies of clothing of the specified size in storage"""
    try:
        return get(storage, size)
    except ValueError:
        return 0


def select(tree_map: TreeMap, size: int) -> str:
    """find in the storage and give the customer a copy of the clothes of the optimal size"""
    try:
        customer_size = get_lower_bound(tree_map, size)

        instances = get(tree_map, customer_size) - 1
        if instances > 0:
            put(tree_map, customer_size, instances)
        else:
            remove(tree_map, customer_size)

        return str(customer_size)

    except ValueError:
        raise ValueError("SORRY")


def detect_command(storage: TreeMap, command: str) -> str:
    """detect command and use it"""
    write_line = ""

    try:
        if command.split()[0] == "ADD":
            size, count = command.split()[1:]
            add_to_storage(storage, int(size), int(count))
        elif command.split()[0] == "SELECT":
            size = command.split()[1]
            write_line = str(select(storage, int(size)))
        elif command.split()[0] == "GET":
            size = command.split()[1]
            write_line = str(get_from_storage(storage, int(size)))
        else:
            write_line = "SORRY"
    except ValueError:
        write_line = "SORRY"
    return write_line


def write_file(storage: TreeMap, storage_name: str, output_name: str) -> None:
    with open(output_name, "w") as output_file:
        with open(storage_name, "r") as storage_file:
            command_number = int(storage_file.readline())
            for i in range(command_number):
                command = storage_file.readline()
                line = detect_command(storage, command.strip())
                if line:
                    output_file.write(line + "\n")


def main():
    storage = create_tree_map()
    write_file(storage, STORAGE_FILE, OUTPUT_FILE)


if __name__ == "__main__":
    main()
