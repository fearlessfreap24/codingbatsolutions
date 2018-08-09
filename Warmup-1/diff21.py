def diff21(n):
    if n > 21:
        return (n-21)*2
    return 21-n


if __name__ == "__main__":
    print(diff21(19))  # 2
    print(diff21(10))  # 11
    print(diff21(21))  # 0
