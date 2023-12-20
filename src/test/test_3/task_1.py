from src.test.test_3.sprite_module import *


def main():
    try:
        size = input("Enter size of square sprite: ")

        try:
            size = int(size)
        except Exception:
            raise ValueError("size must be integer")

        if size <= 0:
            raise ValueError("size must be more then 0")

        user_input = ""

        while user_input == "":
            symmetry = random.choice(("vertical", "horizontal", "complete"))
            if symmetry == "vertical":
                sprite = vertical_symmetry(size)
            elif symmetry == "horizontal":
                sprite = horizontal_symmetry(size)
            else:
                sprite = complete_symmetry(size)

            display(sprite)
            user_input = input(
                "press Enter for new sprite. Enter something else for closing program "
            )
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
