def no_teen_sum(a, b, c):
    if a <= 19 and a >= 13:
        if a == 15 or a == 16:
            fix_teen(a)
    if b <= 19 and b >= 13:
        if b == 15 or b == 16:
            fix_teen(b)
    if c <= 19 and c >= 13:
        if c == 15 or c == 16:
            fix_teen (c)

def fix_teen(n):


if __name__ == "__main__":
    print(no_teen_sum(1, 2, 3)) # 6
    print(no_teen_sum(2, 13, 1)) # 3
    print(no_teen_sum(2, 1, 14)) # 3