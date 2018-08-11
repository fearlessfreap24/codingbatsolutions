def missing_char(str, n):
    ret = ''
    for i in range(len(str)):
        if i == n:
            continue
        else:
            ret += str[i]

    return ret


if __name__ == "__main__":
    print(missing_char('kitten', 1))  # 'ktten'
    print(missing_char('kitten', 0))  # 'itten'
    print(missing_char('kitten', 4))  # 'kittn'
