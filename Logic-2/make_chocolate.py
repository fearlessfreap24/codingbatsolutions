def make_chocolate(small, big, goal):
    if goal > (big * 5) + small:
        return -1
    goalmod = goal % 5
    if goalmod > small:
        return -1
    return goal - (big * 5)

if __name__ == "__main__":
    print(make_chocolate(4, 1, 9)) # 4
    print(make_chocolate(4, 1, 10)) # -1
    print(make_chocolate(4, 1, 7)) # 2