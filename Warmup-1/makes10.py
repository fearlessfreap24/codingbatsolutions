def makes10(a, b):
    #
    # original solution
    #
    # if a == 10 or b == 10:
    #    return True
    # if a+b == 10:
    #    return True
    # return False

    return a == 10 or b == 10 or a+b == 10


if __name__ == "__main__":
    if makes10(9, 10):  # True
        print("true")
    else:
        print("false")
    if makes10(9, 9):  # False
        print("true")
    else:
        print("false")
    if makes10(1, 9):  # True
        print("true")
    else:
        print("false")