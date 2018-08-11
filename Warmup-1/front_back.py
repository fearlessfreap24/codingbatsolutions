def front_back(str):
    if len(str) > 1:
        return str[len(str)-1:len(str)]+str[1:len(str)-1]+str[:1]
    return str


if __name__ == "__main__":
    print(front_back('code'))  # 'eodc'
    print(front_back('a'))  # 'a'
    print(front_back('ab'))  # 'ba'
