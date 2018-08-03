def string_bits(str):
    newstr = ""
    for i in range(len(str)):
        if i%2 == 0:
            newstr += str[i]
    return newstr



if __name__ == "__main__":
    print(string_bits('Hello'))
    print(string_bits('Hi'))
    print(string_bits('Heeololeo'))