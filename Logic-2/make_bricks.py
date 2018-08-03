def make_bricks(small, big, goal):
    modgoal = goal // 5 # goal mod 5 to determine how many big bricks
    # print("{} + {} = {}".format(big*5,small, (big*5)+small))
    # print("modgoal = {}, big = {}".format(modgoal, big))
    # print("modgoal <= big = {}".format(modgoal <= big))
    # print("(5*big)+small >= goal = {}".format((5*big)+small >= goal))
    return big <= modgoal and (5*big)+small >= goal



if __name__ == "__main__":
    if make_bricks(3, 1, 8):
        print("true")
    else:
        print("false")
    if make_bricks(3, 1, 9):
        print("true")
    else:
        print("false")
    if make_bricks(3, 2, 10):
        print("true")
    else:
        print("false")
    if make_bricks(6, 1, 11):
        print("true")
    else:
        print("false")