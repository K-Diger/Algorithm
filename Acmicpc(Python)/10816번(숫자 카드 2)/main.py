# import sys
#
# from collections import deque
#
# input = sys.stdin.readline
#
# # --------------------------------------------------
#
# n = int(input())
# sang_geun = deque(map(int, input().split()))
#
# m = int(input())
# target = deque(map(int, input().split()))
#
# # --------------------------------------------------
#
# answer = deque()
#
# for i in range(m):
#     answer.append(sang_geun.count(target[i]))
#
# for item in answer:
#     print(item, end=" ")
#
# # --------------------------------------------------
#
# answer = deque(0 for i in range(m))
#
# for i in range(n):
#     for j in range(m):
#         if sang_geun[i] == target[j]:
#             answer[j] += 1
#
# for item in answer:
#     print(item, end=" ")
#
# # --------------------------------------------------

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# sang_geun = list(map(int, input().split()))
#
# m = int(input())
# target = list(map(int, input().split()))
#
# correct = {item: 0 for item in sang_geun}
#
# for item in sang_geun:
#     if item in target:
#         # correct[item] = correct[item] + 1
#         correct[item] = correct.get(item) + 1
#
# for item in correct:
#     print(item, end=" ")

import sys

input = sys.stdin.readline

n = int(input())
sang_geun = list(map(int, input().split()))

m = int(input())
target = list(map(int, input().split()))

correct = {item: 0 for item in sang_geun}

for item in sang_geun:
    if item in correct:
        correct[item] += 1

for item in target:
    if item in correct:
        print(correct[item], end=" ")
    else:
        print(0, end=" ")

# print()
# print(correct)
#
# for item in correct:
#     if item in target:
#         # print(correct[item], end=" ")
#         print("item = ", item)
#         print(correct[item])
#     else:
#         print(0, end=" ")


# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# sang_geun = list(map(int, input().split()))
#
# m = int(input())
# target = list(map(int, input().split()))
#
# correct = {item: 0 for item in sang_geun}
#
# for item in sang_geun:
#     if item in correct:
#         correct[item] += 1
#
# for item in correct:
#     if item in target:
#         print(correct[item], end=" ")
#     else:
#         print(0, end=" ")