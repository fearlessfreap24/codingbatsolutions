def combo_string(a, b):
    #
    # old code
    #
    # if len(a) < len(b):
    #    return a+b+a
    # else:
    #    return b+a+b

    # used ternary operator
    retstr = a+b+a if len(a) < len(b) else b+a+b

    return retstr


if __name__ == "__main__":
    print(combo_string('Hello', 'hi'))  # 'hiHellohi'
    print(combo_string('hi', 'Hello'))  # 'hiHellohi'
    print(combo_string('aaa', 'b'))  # 'baaab'