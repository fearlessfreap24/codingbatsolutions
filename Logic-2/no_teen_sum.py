def no_teen_sum(a, b, c):
    sum = 0
    if a in range(13,20):
        if a == 15 or a == 16:
            sum += a
        else:
            sum += 0
    else:
        sum += a
    if b in range(13,20):
        if b == 15 or b == 16:
            sum += b
        else:
            sum += 0
    else:
        sum += b
    if c in range(13,20):
        if c == 15 or c == 16:
            sum += c
        else:
            sum += 0
    else:
        sum += c
    return sum



if __name__ == "__main__":
    print(no_teen_sum(1, 2, 3)) # 6
    print(no_teen_sum(2, 13, 1)) # 3
    print(no_teen_sum(2, 1, 14)) # 3