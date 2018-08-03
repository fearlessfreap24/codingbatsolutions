def has23(nums):
    return 2 in nums or 3 in nums



if __name__ == "__main__":
    if has23([2, 5]):
        print("true")
    else:
        print("false")
    if has23([4, 3]):
        print("true")
    else:
        print("false")
    if has23([4, 5]):
        print("true")
    else:
        print("false")