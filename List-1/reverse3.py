def reverse3(nums):
    return [nums[-1], nums[-2], nums[-3]]


if __name__ == "__main__":
    print("{} : {}".format([1,2,3],reverse3([1, 2, 3])))
    print("{} : {}".format([5,11,9],reverse3([5, 11, 9])))
    print("{} : {}".format([7,0,0],reverse3([7, 0, 0])))