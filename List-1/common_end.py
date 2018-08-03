def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]



if __name__ == "__main__":
    if common_end([1, 2, 3], [7, 3]):
        print("true")
    else:
        print("false")
    if common_end([1, 2, 3], [7, 3, 2]):
        print("true")
    else:
        print("false")
    if common_end([1, 2, 3], [1, 3]):
        print("true")
    else:
        print("false")
    if common_end([1, 2, 3], [1]):
        print("true")
    else:
        print("false")
