def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    if num % 10 >= 0 and num % 10 <= 4:
        # print("less {}".format(num // 10))
        return num - (num % 10)
    if num % 10 >= 5 and num % 10 <= 9:
        # print("more {}".format(num // 10))
        return num - (num % 10) + 10

if __name__ == "__main__":
    print(round_sum(16, 17, 18)) # 60
    print(round_sum(12, 13, 14)) # 30
    print(round_sum(6, 4, 4)) # 10