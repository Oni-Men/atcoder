from collections import deque


def new_node(is_root=False):
    node = {
        "op": None,
        "l": None,
        "r": None
    }
    if is_root:
        node["c"] = None
    return node


def make_tree(s, is_root=False):
    if s[0] in "1234567890":
        return int(s[0]), s[1:]

    node = new_node(is_root)
    node["l"], s = make_tree(s)

    node["op"] = s[0]
    s = s[1:]

    if is_root:
        node["c"], s = make_tree(s)
        s = s[1:]

    node["r"], s = make_tree(s)

    return node


def solve():
    s = input()
    if s == "-1":
        return False

    root = make_tree(s)
    return True


while solve():
    pass
