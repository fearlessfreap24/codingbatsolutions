def lone_sum(a,b,c):
    if a == b and b == c:
        # print("a == b and b == c")
        return a - b
    if a == b:
        # print("a == b")
        return c
    if a == c:
        # print("a == c")
        return b
    if b == c:
        # print("b == c")
        return a
    return a + b + c


if __name__ == "__main__":
    print(lone_sum(1, 2, 3))
    print(lone_sum(3, 2, 3))
    print(lone_sum(3, 3, 3))
