def parrot_trouble(talking, hour):
    # this was my original answer
    #
    #if ((hour < 7) or (hour > 20)) and talking:
    #    return True
    # return False
    #
    return ((hour < 7) or (hour > 20)) and talking


if __name__ == "__main__":
    if parrot_trouble(True, 6):  # True
        print("true")
    else:
        print("false")
    if parrot_trouble(True, 7):  # False
        print("true")
    else:
        print("false")
    if parrot_trouble(False, 6):  # False
        print("true")
    else:
        print("false")