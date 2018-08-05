def close_far(a, b, c): # i had to look up an explanation because I did not understand the problem
    return (abs(a-b) <= 1 and abs(a-c) >= 2 and abs(b-c) >= 2) or (abs(a-c) <= 1 and abs(a-b) >= 2 and abs(b-c) >= 2)

if __name__ == "__main__":
    if close_far(1, 2, 10): # True
        print("true")
    else:
        print("false")
    if close_far(1, 2, 3): # False
        print("true")
    else:
        print("false")
    if close_far(4, 1, 3): # True
        print("true")
    else:
        print("false")