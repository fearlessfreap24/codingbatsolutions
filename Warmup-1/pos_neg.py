def pos_neg(a, b, negative):
    #
    # old answer
    #
    # if (a >-1 and b<0) or (a<0 and b>-1):
    #    if negative:
    #        return False
    #    return True
    #
    # if (a<0 and b<0) and negative:
    #    return True
    # return False

    return (a < 0 and b < 0 and negative) or (a < 0 and b >= 0 and not negative) or (a >= 0 and b < 0 and not negative)


if __name__ == "__main__":
    if pos_neg(1, -1, False):  # True
        print("true")
    else:
        print("false")
    if pos_neg(-1, 1, False):  # True
        print("true")
    else:
        print("false")
    if pos_neg(-4, -5, True):  # True
        print("true")
    else:
        print("false")