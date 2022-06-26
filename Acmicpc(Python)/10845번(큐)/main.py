from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

instruction = ""
value = ""

queue = deque()

for _ in range(n):

    input_value = input()

    if " " in input_value:
        instruction = input_value.split()[0].strip("\n")
        value = input_value.split()[1].strip("\n")
    else:
        instruction = input_value.strip("\n")

    if instruction == "push":
        queue.append(value)

    elif instruction == "pop":
        if (len(queue)) == 0:
            print(-1)
        else:
            print(queue.popleft())

    elif instruction == "size":
        print(len(queue))

    elif instruction == "empty":

        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif instruction == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    elif instruction == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue)-1])

