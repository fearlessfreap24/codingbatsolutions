def max_end3(nums):
    if nums[0] >= nums[-1]:
        return [nums[0],nums[0],nums[0]]
    if nums[0] < nums[-1]:
        return [nums[-1],nums[-1],nums[-1]]



if __name__ == "__main__":
    print("{} :{}".format([1,2,3],max_end3([1, 2, 3])))
    print("{} : {}".format([11,5,9],max_end3([11, 5, 9])))
    print("{} : {}".format([2,11,3],max_end3([2, 11, 3])))
    print("{} : {}".format([2,11,2],max_end3([2, 11, 2])))