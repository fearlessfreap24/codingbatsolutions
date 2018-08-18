def make_tags(tag, word):
    return "<{}>".format(tag)+word+"</{}>".format(tag)


if __name__ == "__main__":
    print(make_tags('i', 'Yay'))  # '<i>Yay</i>'
    print(make_tags('i', 'Hello'))  # '<i>Hello</i>'
    print(make_tags('cite', 'Yay'))  # '<cite>Yay</cite>'
