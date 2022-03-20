while True:
    case_input = input()

    if case_input == str(0):
        break
    elif case_input == case_input[::-1]:
        print("yes")
    else:
        print("no")