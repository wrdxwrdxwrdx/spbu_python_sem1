from hash_table import *


def main():
    try:
        hash_table = create_hash_table()

        put(hash_table, "may 1", 12)
        put(hash_table, "1 may", 121)
        put(hash_table, "may 2", 15)
        put(hash_table, "may 3", 15)
        put(hash_table, "may 4", 15)

        print(items(hash_table))

        remove(hash_table, "1 may")

        print(items(hash_table))
        print(has_key(hash_table, "may 4"))
        print(has_key(hash_table, "may 10"))

        delete_hash_table(hash_table)

        print(items(hash_table))
        print(get(hash_table, "may 4"))

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
