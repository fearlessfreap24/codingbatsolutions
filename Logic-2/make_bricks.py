def make_bricks(small, big, goal):

    # watched part of coding bat video

    if goal > (big * 5) + small:
        return False

    goalmod = goal % 5
    if goalmod > small:
        return False

    return True




if __name__ == "__main__":
    print("3,2,8")
    if make_bricks(3, 2, 8):
        print("true")
    else:
        print("false")
    print("3,1,9")
    if make_bricks(3, 1, 9):
        print("true")
    else:
        print("false")
    print("3,2,10")
    if make_bricks(3, 2, 10):
        print("true")
    else:
        print("false")
    print("6,1,11")
    if make_bricks(6, 1, 11):
        print("true")
    else:
        print("false")
