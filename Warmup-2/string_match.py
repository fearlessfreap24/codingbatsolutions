def string_match(a,b):
    count = 0
    for i in range(len(a)-1):
        print("a = {}, b = {}".format(a[i:i+2], b[i:i+2]))
        if a[i:i+2] == b[i:i+2]:
            count+=1
    return count



if __name__ == "__main__":
    print(string_match('xxcaazz', 'xxbaaz'))
    print(string_match('abc', 'abc'))
    print(string_match('abc', 'axc'))