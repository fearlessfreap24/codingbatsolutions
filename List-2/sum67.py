def sum67(nums):
    if 6 not in nums:
        return sum(nums)
    else:
        ret = 0
        flag = False
        for num in nums:
            if num == 6:
                flag = True
                continue
            elif num == 7 and flag:
                flag = False
                continue

            if not flag:
                ret += num

        return ret

# I had to look this one up. it is a slight variation of what I found.
# I initially have it checking if 6 exists in the list and if it doesn't return the sum of the list
# I started with a loop and got the initial index of the first 6 and 7.
# I had it working it there was only one 6 or 7. There lies the problem. The 4th print statement
# has 2 6's and 7's.


if __name__ == "__main__":
    print(sum67([1, 2, 2]))  # 5
    print(sum67([1, 2, 2, 6, 99, 99, 7]))  # 5
    print(sum67([1, 1, 6, 7, 2]))  # 4
    print(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))  # 2
