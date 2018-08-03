def string_splosion(str):
    result = ""
    for i in range(len(str)):
        result += str[:i+1]
    return result



if __name__ == "__main__":
    print(string_splosion('Code'))
    print(string_splosion('abc'))
    print(string_splosion('ab'))