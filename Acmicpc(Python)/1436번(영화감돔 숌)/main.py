# answer = list()
#
# for i in range(n):
#     answer.append(str(i) + "666")
#
#
# for i in range(n):
#     answer.append("666" + str(i))
#
# for i in range(n):
#     answer.append(str(i) + "666" + str(i))
#
# answer = set(answer)
#
# answer = list(map(int, answer))
#
# answer.sort()
#
# print(answer)
#
# print(answer[n-1])


import sys

input = sys.stdin.readline

n = int(input())

answer = list()

i = int(666)

while True:

    if "666" in str(i):
        answer.append(i)
    i += 1

    if len(answer) == n:
        print(answer[n - 1])
        break
