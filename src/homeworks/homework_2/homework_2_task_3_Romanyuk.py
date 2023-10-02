from os.path import exists


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"{self.val}{self.next}"

    def start_with(self, start):
        head = self
        while start and head:
            if start.val != head.val:
                return False
            start, head = start.next, head.next
        return True

    def length(self):
        head = self
        count = 0
        while head:
            count += 1
            head = head.next
        return count


def string_to_node(line):
    head = None
    previous = None
    for i in line:
        current = ListNode(i)
        if head is None:
            head = current
        if previous is not None:
            previous.next = current
        previous = current
    return head


def delete(start, finish, dna):
    head = ListNode(None)
    head.next = dna

    # detect is "start" - first element
    if not dna.start_with(start):
        is_answer_none = False
        head.next = dna
    else:
        is_answer_none = True

    previous = dna

    # find start element
    while not dna.start_with(start):
        previous = dna
        dna = dna.next

    # find finish element
    while not dna.start_with(finish):
        dna = dna.next

    # skip finish element
    for i in range(finish.length()):
        dna = dna.next

    previous.next = dna

    if is_answer_none:
        return dna
    return head.next


def insert(start, fragment, dna):
    head = ListNode(None)
    head.next = dna

    # find start element
    while not dna.start_with(start):
        previous = dna
        dna = dna.next

    # skip start element
    for i in range(start.length()):
        previous = dna
        dna = dna.next
    previous.next = fragment

    # find end of fragment
    last_fragment = fragment
    for i in range(fragment.length() - 1):
        last_fragment = fragment.next
        fragment = fragment.next
    last_fragment.next = dna

    return head.next


def replace(template, fragment, dna):
    head = ListNode(None)

    # detect is "template" - first element
    if dna.start_with(template):
        # skip template
        for i in range(template.length()):
            dna = dna.next
        head.next = fragment
    else:
        head.next = dna

        # find template
        while not dna.start_with(template):
            previous = dna
            dna = dna.next

        # skip template
        for i in range(template.length()):
            dna = dna.next
        previous.next = fragment

    # find end of fragment
    last_fragment = fragment
    for i in range(fragment.length() - 1):
        last_fragment = fragment.next
        fragment = fragment.next

    last_fragment.next = dna
    return head.next


if __name__ == "__main__":
    read_file_name = input("file with commands [src].txt: ")
    write_file_name = input("output file [dst].txt: ")

    if exists(read_file_name):
        with open(write_file_name, "w") as write_file:
            with open(read_file_name, "r") as read_file:
                length_dna = int(read_file.readline())
                dna = string_to_node(read_file.readline().strip())
                command_number = int(read_file.readline())
                for i in range(command_number):
                    line = read_file.readline().split()
                    if line[0] == "DELETE":
                        dna = delete(
                            string_to_node(line[1]), string_to_node(line[2]), dna
                        )
                    elif line[0] == "INSERT":
                        dna = insert(
                            string_to_node(line[1]), string_to_node(line[2]), dna
                        )
                    elif line[0] == "REPLACE":
                        dna = replace(
                            string_to_node(line[1]), string_to_node(line[2]), dna
                        )
                    write_file.write(str(dna)[:-4] + "\n")
        print(f"{write_file_name} done")
    else:
        print(f"{read_file_name} does not exist")
