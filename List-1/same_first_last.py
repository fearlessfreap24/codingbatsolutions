def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]



if __name__ == "__main__":
    if same_first_last([1, 2, 3]):
        print("true")
    else:
        print("false")
    if same_first_last([1, 2, 3, 1]):
        print("true")
    else:
        print("false")
    if same_first_last([1, 2, 1]):
        print("true")
    else:
        print("false")