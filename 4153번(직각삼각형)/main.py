import sys

while True:
    test_input = list(map(int, sys.stdin.readline().split()))
    test_input.sort()

    if test_input[0] == 0 and test_input[1] == 0 and test_input[2] == 0:
        break
    elif test_input[0] ** 2 + test_input[1] ** 2 == test_input[2] ** 2:
        print("right")
    else:
        print("wrong")