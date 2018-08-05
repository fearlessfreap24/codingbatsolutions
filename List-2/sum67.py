def sum67(nums):
    if 6 not in nums:
        return sum(nums)
    else:
        sixes = nums.count(6)
        sevs = nums.count(7)
        six = nums.index(6)
        sev = nums.index(7)
        newnums = []
        for i in range(sixes):
            newnums += nums[:six]
            nums = nums[six + 1:sev]
        return sum(newnums)


if __name__ == "__main__":
    print(sum67([1, 2, 2]))  # 5
    print(sum67([1, 2, 2, 6, 99, 99, 7]))  # 5
    print(sum67([1, 1, 6, 7, 2]))  # 4
