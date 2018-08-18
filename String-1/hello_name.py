def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == "__main__":
    print(hello_name('Bob'))  # 'Hello Bob!'
    print(hello_name('Alice'))  # 'Hello Alice!'
    print(hello_name('X'))  # 'Hello X!'
