def front3(str):
    #
    # old code
    #
    # newstr = str[:3]
    # return newstr+newstr+newstr

    return str[:3]*3


if __name__ == "__main__":
    print(front3('Java'))  # 'JavJavJav'
    print(front3('Chocolate'))  # 'ChoChoCho'
    print(front3('abc'))  # 'abcabcabc'