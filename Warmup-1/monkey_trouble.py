def monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or (not a_smile and not b_smile)


# return true if a and b or not a and not b


if __name__ == "__main__":
    if monkey_trouble(True, True):  # True
        print("true")
    else:
        print("false")
    if monkey_trouble(False, False):  # True
        print("true")
    else:
        print("false")
    if monkey_trouble(True, False):  # False
        print("true")
    else:
        print("false")