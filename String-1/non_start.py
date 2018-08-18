def non_start(a, b):
    return a[1:]+b[1:]


if __name__ == "__main__":
    print(non_start('Hello', 'There'))  # 'ellohere'
    print(non_start('java', 'code'))  # 'avaode'
    print(non_start('shotl', 'java'))  # 'hotlava'
