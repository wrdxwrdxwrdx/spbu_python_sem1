from dataclasses import dataclass, field
from typing import Optional
from collections import namedtuple


@dataclass
class Node:
    name: str = ""
    children: list["Node"] = field(default_factory=lambda: [])


@dataclass
class ParseTree:
    root: Optional[Node] = None


Output = namedtuple("output", "pointer node")


def pretty_print(tree: ParseTree):
    def pretty_print_node(space_number: int, node: Node):
        for child in node.children:
            print("." * (space_number + 4), child.name)
            pretty_print_node(space_number + 4, child)

    if tree.root:
        print(tree.root.name)
        pretty_print_node(0, tree.root)
    else:
        raise ValueError("Tree is Empty")


def _start(pointer: int, tokens: list[str]) -> Optional[Output]:
    t_pointer, t_node = _t(pointer, tokens)
    sum_pointer, sum_node = _sum(t_pointer, tokens)
    return Output(
        pointer=sum_pointer,
        node=Node("START", [t_node, sum_node]),
    )


def _sum(pointer: int, tokens: list[str]) -> Optional[Output]:
    if pointer < len(tokens) and tokens[pointer] == "+":
        if _t(pointer + 1, tokens):
            t_pointer, t_node = _t(pointer + 1, tokens)
            if _sum(t_pointer, tokens):
                sum_pointer, sum_node = _sum(t_pointer, tokens)
                return Output(
                    pointer=sum_pointer,
                    node=Node("SUM", [Node("+"), t_node, sum_node]),
                )
    if pointer >= len(tokens) or tokens[pointer] != "+":
        return Output(
            pointer=pointer,
            node=Node("SUM", [Node("eps")]),
        )
    raise ValueError(f"incorrect sum")


def _t(pointer: int, tokens: list[str]) -> Optional[Output]:
    token_pointer, token_node = _token(pointer, tokens)
    prod_pointer, prod_node = _prod(token_pointer, tokens)
    return Output(
        pointer=prod_pointer,
        node=Node("T", [token_node, prod_node]),
    )


def _prod(pointer: int, tokens: list[str]) -> Optional[Output]:
    if pointer < len(tokens) and tokens[pointer] == "*":
        if _token(pointer + 1, tokens):
            token_pointer, token_node = _token(pointer + 1, tokens)
            if _prod(token_pointer, tokens):
                prod_pointer, prod_node = _prod(token_pointer, tokens)
                return Output(
                    pointer=prod_pointer,
                    node=Node("PROD", [Node("*"), token_node, prod_node]),
                )
        else:
            raise ValueError(f"invalid character after '*', index {pointer+1}")
    if pointer >= len(tokens) or tokens[pointer] != "*":
        return Output(
            pointer=pointer,
            node=Node("PROD", [Node("eps")]),
        )
    raise ValueError(f"incorrect prod")


def _token(pointer: int, tokens: list[str]) -> Optional[Output]:
    if pointer >= len(tokens):
        raise ValueError(f"incorrect mathematical expression")
    if pointer < len(tokens) and tokens[pointer] == "(":
        if _start(pointer + 1, tokens):
            start_pointer, start_node = _start(pointer + 1, tokens)
            if start_pointer < len(tokens) and tokens[start_pointer] == ")":
                return Output(
                    pointer=start_pointer + 1,
                    node=Node("TOKEN", [Node("("), start_node, Node(")")]),
                )
    if tokens[pointer].isdigit():
        return Output(
            pointer=pointer + 1,
            node=Node("TOKEN", [Node(f"id({tokens[pointer]})")]),
        )
    raise ValueError(f"incorrect token {tokens[pointer]}")


def parse(tokens: list[str]) -> ParseTree:
    if tokens:
        return ParseTree(_start(0, tokens).node)
    else:
        raise ValueError("Empty token list")
