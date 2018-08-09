def sum_double(a, b):
    if a == b:
        return (a+b)*2
    return (a+b)


if __name__ == "__main__":
    print(sum_double(1, 2))  # 3
    print(sum_double(3, 2))  # 5
    print(sum_double(2, 2))  # 8