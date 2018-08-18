def first_half(str):
    # a = int(len(str)/2)
    # return str[:a]

    return str[:int(len(str)/2)]


if __name__ == "__main__":
    print(first_half('WooHoo'))  # 'Woo'
    print(first_half('HelloThere'))  # 'Hello'
    print(first_half('abcdef'))  # 'abc'
