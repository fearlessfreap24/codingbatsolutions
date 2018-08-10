def near_hundred(n):
    #
    # original solution
    #
    # if abs(n-100) <= 10 or abs(200-n) <= 10:
    #    return True
    # return False

    return abs(n-100) <= 10 or abs(200-n) <= 10


if __name__ == "__main__":
    if near_hundred(93):  # True
        print("true")
    else:
        print("false")
    if near_hundred(90):  # True
        print("true")
    else:
        print("false")
    if near_hundred(89):  # False
        print("true")
    else:
        print("false")