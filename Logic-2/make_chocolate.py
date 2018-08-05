def make_chocolate(small, big, goal):
    if (big * 5) + small >= goal:
        return goal % 5
    else:
        return -1

if __name__ == "__main__":
    print(make_chocolate(4, 1, 9)) # 4
    print(make_chocolate(4, 1, 10)) # -1
    print(make_chocolate(4, 1, 7)) # 2