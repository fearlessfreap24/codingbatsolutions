def count_evens(nums):
    sum = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            sum += 1
    return sum


if __name__ == "__main__":
    print(count_evens([2, 1, 2, 3, 4]))  # 3
    print(count_evens([2, 2, 0]))  # 3
    print(count_evens([1, 3, 5]))  # 0
