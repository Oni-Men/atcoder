import re


def solve():
    str = input()
    if str == ".":
        return False
    str = re.sub("[a-zA-Z ]", "", str[:-1])
    while str.find("()") != -1 or str.find("[]") != -1:
        str = re.sub("\(\)|\[\]", "", str)
    print("yes" if len(str) == 0 else "no")
    return True


while solve():
    pass
