def array_front9(nums):
    return 9 in nums[0:4]



if __name__ == "__main__":
    if array_front9([1, 2, 9, 3, 4]):
        print("true")
    else:
        print("false")
    if array_front9([1, 2, 3, 4, 9]):
        print("true")
    else:
        print("false")
    if array_front9([1, 2, 3, 4, 5]):
        print("true")
    else:
        print("false")
    if array_front9([1, 2, 9]):
        print("true")
    else:
        print("false")
    if array_front9([1, 2, 3]):
        print("true")
    else:
        print("false")