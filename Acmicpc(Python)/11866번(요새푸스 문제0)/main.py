# 1 2 3 4 5 6 7

# 전체 길이 = 7
# 삭제할 인덱스 = 2
# 삭제 되는 값 = 3

# 1 2 4 5 6 7

# 전체 길이 = 6
# 삭제할 인덱스 = 5
# 삭제 되는 값 = 6

# 1 2 4 5 7

# 전체 길이 = 5
# 삭제할 인덱스 = 1 = (5 + 3) % 5
# 삭제 되는 값 = 2

# 1 4 5 7

# 전체 길이 = 4
# 삭제할 인덱스 = 3 = (4 + 3) % 4
# 삭제 되는 값 = 7

# 1 4 5

# 전체 길이 = 3
# 삭제할 인덱스 = 0 = (3 + 3) % 3
# 삭제 되는 값 = 1


from collections import deque

n, k = map(int, input().split())

circle = deque(i for i in range(1, n + 1))
answer = deque()


while circle:
    for i in range(k-1):
        circle.append(circle.popleft())
    answer.append(circle.popleft())

print("<", end="")

for index in range(len(answer) - 1):
    print(answer[index], end=", ")
print(answer[len(answer) - 1], end="")

print(">", end="")
