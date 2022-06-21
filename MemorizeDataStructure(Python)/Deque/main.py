from collections import deque

deque = deque()

deque.append(1.1)
deque.append(1)
deque.append("1")
deque.append(11)

print(deque)

deque.rotate(-1)

print(deque)