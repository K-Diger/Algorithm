# import sys
#
#
# input = sys.stdin.readline
# stack = list()
#
# n = int(input())
# instruction = ""
# value = ""
#
# for i in range(n):
#     input_value = input()
#
#     if " " in input_value:
#         instruction = input_value.split(" ")[0]
#         value = input_value.split(" ")[1]
#     else:
#         instruction = input_value.strip('\n')
#
#
#     if instruction == "push":
#         stack.append(value)
#
#     elif instruction == "pop":
#         if len(stack) == 0:
#             print("-1")
#         else:
#             print(stack[len(stack)-1].split("\n")[0])
#             stack.pop()
#
#     elif instruction == "top":
#         if len(stack) == 0:
#             print("-1")
#         else:
#             print(stack[len(stack)-1].split("\n")[0])
#
#     elif instruction == "size":
#         print(len(stack))
#
#     elif instruction == "empty":
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#     else:
#         print("잘못 입력")

import sys

input = sys.stdin.readline
stack = list()

n = int(input())
instruction = ""
value = ""

for i in range(n):
    input_value = input()

    if " " in input_value:
        instruction = input_value.split(" ")[0]
        value = input_value.split(" ")[1]
    else:
        instruction = input_value.strip('\n')

    if instruction == "push":
        stack.append(value)

    elif instruction == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            # print(stack[len(stack)-1].split("\n")[0])
            print(stack.pop())

    elif instruction == "top":
        if len(stack) == 0:
            print("-1")
        else:
            # print(stack[len(stack)-1].split("\n")[0])
            print(stack[-1])

    elif instruction == "size":
        print(len(stack))

    elif instruction == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        print("잘못 입력")