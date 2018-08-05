def make_chocolate(small, big, goal):

    # not enough bricks
    if big * 5 + small < goal:
        return -1

    # not enough small bricks
    goalmod = goal % 5
    if goalmod > small:
        return -1

    # enough small bricks
    if big < goal // 5:
        return goal - (big * 5)
    if big >= goal // 5:
        return goal % 5


if __name__ == "__main__":
    print(make_chocolate(4, 1, 9))  # 4
    print(make_chocolate(4, 1, 10))  # -1
    print(make_chocolate(4, 1, 7))  # 2
    print(make_chocolate(6, 2, 7))  # 2
    print(make_chocolate(7, 1, 12))  # 7
