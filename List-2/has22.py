def has22(nums):
    flag = False

    for num in nums:
        if num == 2 and not flag:
            flag = True
            continue
        elif num == 2 and flag:
            return True
        else:
            flag = False
    return False


if __name__ == "__main__":
    if has22([1, 2, 2]):  # True
        print("true")
    else:
        print("false")
    if has22([1, 2, 1, 2]):  # False
        print("true")
    else:
        print("false")
    if has22([2, 1, 2]):  # False
        print("true")
    else:
        print("false")
