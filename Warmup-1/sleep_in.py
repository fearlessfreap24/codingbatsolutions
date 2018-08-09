def sleep_in(weekday, vacation):
    return vacation or not weekday


# since vacation is evaluated first, if it is true it will return true.
# because we need to know when it is not a weekday, returning the value of not weekday will
# return true if it is a weekend.


if __name__ == "__main__":
    if sleep_in(False, False):  # True
        print("true")
    else:
        print("false")
    if sleep_in(True, False):  # False
        print("true")
    else:
        print("false")
    if sleep_in(False, True):  # True
        print("true")
    else:
        print("false")