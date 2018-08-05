def centered_average(nums):

    # sort the array of ints
    newnums = sorted(nums)

    # get the length minus the first and last position
    length = len(newnums) - 2

    # use sum() for add positions 1 through end - 1 and divide by length
    # cast the average to an integer
    return int(sum(newnums[1:-1]) / length)

if __name__ == "__main__":
    print(centered_average([1, 2, 3, 4, 100]))  # 3
    print(centered_average([1, 1, 5, 5, 10, 8, 7]))  # 5
    print(centered_average([-10, -4, -2, -4, -2, 0]))  # -3
