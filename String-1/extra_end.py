def extra_end(str):
    #
    # ole code
    #
    # a = str[-2:]
    # return a+a+a

    return str[-2:]*3


if __name__ == "__main__":
    print(extra_end('Hello'))  # 'lololo'
    print(extra_end('ab'))  # 'ababab'
    print(extra_end('Hi'))  # 'HiHiHi'
