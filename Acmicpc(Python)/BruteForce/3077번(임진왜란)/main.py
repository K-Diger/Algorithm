# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
#
# writing = input().split()
# answer = input().split()
#
# writing_pair = deque()
# answer_pair = deque()
# count = int(0)
#
# for i in range(len(writing) - 1):
#     for j in range(i + 1, len(answer)):
#         writing_pair.append(writing[i] + " " + writing[j])
#         answer_pair.append(answer[i] + " " + answer[j])
#
# while writing_pair:
#     target = writing_pair.popleft()
#     if target in answer_pair:
#         count += 1
#
# print(str(count) + "/" + str(len(answer_pair)))


import sys

input = sys.stdin.readline

n = int(input())

answer = dict(zip(input().split(), [i for i in range(n)]))
writing = input().split()
count = int(0)

for i in range(n - 1):
    for j in range(i + 1, n):
        if answer[writing[i]] < answer[writing[j]]:
            count += 1

print(count, "/", n * (n - 1) // 2, sep="")