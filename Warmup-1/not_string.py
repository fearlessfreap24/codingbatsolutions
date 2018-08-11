def not_string(str):
    if str.startswith('not'):
        return str
    return ("not " + str)


if __name__ == "__main__":
    print(not_string('candy'))  # 'not candy'
    print(not_string('x'))  # 'not x'
    print(not_string('not bad'))  # 'not bad'
