

#입력 : <<BP<A>>Cd-
#출력 : BAPC

from collections import deque

test = deque()
test.append(10)
test.append((test.popleft()), 0)
print(test)