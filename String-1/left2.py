def left2(str):
    #
    # old code
    #
    # if len(str) > 2:
    #    return str[2:]+str[:2]
    # else:
    #    return str

    return str[2:]+str[:2]


if __name__ == "__main__":
    print(left2('Hello'))  # 'lloHe'
    print(left2('java'))  # 'vaja'
    print(left2('Hi'))  # 'Hi'
