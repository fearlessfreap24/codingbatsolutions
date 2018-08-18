def make_out_word(out, word):
    return out[0:2]+word+out[2:]


if __name__ == "__main__":
    print(make_out_word('<<>>', 'Yay'))  # '<<Yay>>'
    print(make_out_word('<<>>', 'WooHoo'))  # '<<WooHoo>>'
    print(make_out_word('[[]]', 'word'))  # '[[word]]'
