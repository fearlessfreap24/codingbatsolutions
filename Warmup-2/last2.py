def last2(str):
    result = 0
    for i in range(len(str)-2):
        if str[-2:] == str[i:i+2]:
            result += 1
    return result


if __name__ == "__main__":
    print(last2('hixxhi'))
    print(last2('xaxxaxaxx'))
    print(last2('axxxaaxx'))