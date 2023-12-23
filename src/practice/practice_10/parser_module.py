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


def pretty_print(tree: ParseTree):
    def pretty_print_node(space_number: int, node: Node):
        print("." * space_number + node.name)
        for child in node.children:
            pretty_print_node(space_number + 4, child)

    if tree.root:
        pretty_print_node(0, tree.root)
    else:
        raise ValueError("Tree is Empty")


def _start(pointer: int, tokens: list[str]) -> (Node, int):
    t_node, t_pointer = _t(pointer, tokens)
    sum_node, sum_pointer = _sum(t_pointer, tokens)
    return Node("START", [t_node, sum_node]), sum_pointer


def _sum(pointer: int, tokens: list[str]) -> (Node, int):
    if pointer < len(tokens) and tokens[pointer] == "+":
        t_node, t_pointer = _t(pointer + 1, tokens)
        sum_node, sum_pointer = _sum(t_pointer, tokens)
        return Node("SUM", [Node("+"), t_node, sum_node]), sum_pointer
    if pointer >= len(tokens) or tokens[pointer] != "+":
        return Node("SUM", [Node("eps")]), pointer
    raise ValueError(f"incorrect sum")


def _t(pointer: int, tokens: list[str]) -> (Node, int):
    token_node, token_pointer = _token(pointer, tokens)
    prod_node, prod_pointer = _prod(token_pointer, tokens)
    return Node("T", [token_node, prod_node]), prod_pointer


def _prod(pointer: int, tokens: list[str]) -> (Node, int):
    if pointer < len(tokens) and tokens[pointer] == "*":
        token_node, token_pointer = _token(pointer + 1, tokens)
        prod_node, prod_pointer = _prod(token_pointer, tokens)
        return Node("PROD", [Node("*"), token_node, prod_node]), prod_pointer
    if pointer >= len(tokens) or tokens[pointer] != "*":
        return Node("PROD", [Node("eps")]), pointer
    raise ValueError(f"incorrect prod")


def _token(pointer: int, tokens: list[str]) -> (Node, int):
    if pointer >= len(tokens):
        raise ValueError(f"incorrect mathematical expression")
    if pointer < len(tokens) and tokens[pointer] == "(":
        start_node, start_pointer = _start(pointer + 1, tokens)
        if start_pointer < len(tokens) and tokens[start_pointer] == ")":
            return (
                Node("TOKEN", [Node("("), start_node, Node(")")]),
                start_pointer + 1,
            )
    if tokens[pointer].isdigit():
        return Node("TOKEN", [Node(f"id({tokens[pointer]})")]), pointer + 1
    raise ValueError(f"incorrect token {tokens[pointer]}")


def parse(tokens: list[str]) -> ParseTree:
    if tokens:
        return ParseTree(_start(0, tokens)[0])
    else:
        raise ValueError("Empty token list")
