def first_two(str):
    # if len(str) > 1:
    #    return str[0:2]
    # else:
    #    return str

    return str[:2]


if __name__ == "__main__":
    print(first_two('Hello'))  # 'He'
    print(first_two('abcdefg'))  # 'ab'
    print(first_two('ab'))  # 'ab'
    print(first_two('X'))  # 'X'
