def array123(nums):
    list = [1,2,3]
    for i in range(len(nums)-2):
        print(nums[i:i+3])
        if list == nums[i:i+3]:
            return True
    return False




if __name__ == "__main__":
    if array123([1, 1, 2, 3, 1]):
        print("True")
    else:
        print("false")
    if array123([1, 1, 2, 4, 1]):
        print("True")
    else:
        print("false")
    if array123([1, 1, 2, 1, 2, 3]):
        print("True")
    else:
        print("false")