def sum13(nums):
    sum = 0
    for i in range(len(nums)):
        # if i == 0 then i - 1 would br the last element, therefore make sure i > 0 before making this comparison
        if i > 0 and nums[i-1] == 13:
            # conitune allows us to skip over this comparison (i.e. nums[i-1] == 13)
            continue
        # as long as the element is not 13, add it to the sum
        elif nums[i] != 13:
            sum += nums[i]
    return sum


if __name__ == "__main__":
    print(sum13([1, 2, 2, 1]))  # 6
    print(sum13([1, 1]))  # 2
    print(sum13([1, 2, 2, 1, 13]))  # 6
    print(sum13([1, 2, 13, 2, 1, 13]))  # 4
