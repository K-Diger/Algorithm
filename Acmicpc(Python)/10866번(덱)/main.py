from collections import deque
import sys

input = sys.stdin.readline

deque = deque()
instruction = ""
value = ""

n = int(input())

for _ in range(n):

    instruction_value = input()

    if " " in instruction_value:
        instruction = instruction_value.split(" ")[0].strip("\n")
        value = instruction_value.split(" ")[1].strip("\n")
    else:
        instruction = instruction_value.strip("\n")

    if instruction == "push_front":
        deque.appendleft(value)

    elif instruction == "push_back":
        deque.append(value)

    elif instruction == "pop_front":
        if (len(deque)) == 0:
            print(-1)
        else:
            print(deque.popleft())

    elif instruction == "pop_back":
        if (len(deque)) == 0:
            print(-1)
        else:
            print(deque.pop())

    elif instruction == "size":
        print(len(deque))

    elif instruction == "empty":
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    elif instruction == "front":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    elif instruction == "back":
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[len(deque)-1])