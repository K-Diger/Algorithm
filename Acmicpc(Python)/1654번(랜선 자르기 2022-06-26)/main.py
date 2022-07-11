# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# k, n = map(int, input().split())
#
# sik_cable = list()
#
# for _ in range(k):
#     sik_cable.append(int(input()))
#
# answer = deque()
#
# for i in range(sum(sik_cable)//n, 1, -1):
#     count = 0
#     for j in range(k):
#         count += sik_cable[j] // i
#
#         if count >= n:
#             answer.append(i)
#
# print(max(answer))

import sys

input = sys.stdin.readline

k, n = map(int, input().split())
young_sik = [int(input()) for _ in range(k)]

start = 1
end = max(young_sik) + 1

def binary_search(young_sik, start, end, target):

    # start 부터 시작해서, end 직전까지 정답이 있다. == start 가 정답이 된다.
    if end - start <= 1:
        return start

    # mid 의 길이로 짜를때
    mid = (start + end) // 2
    # 몇 개가 나오는가?
    count = 0

    # 1. 이제 직접 잘라보자
    # item = 영식이가 가진 랜선을 순회하는 것.
    # 그걸 mid 로 나눈 몫을 count
    for item in young_sik:
        count += (item // mid)

    # 잘라서 나온 갯수가 target 보다 작으면?
    # mid 값이 너무 큰거다. 즉 중간 분기점에서 오른쪽으로 더 살필 필요가 없다.
    if count < target:
        return binary_search(young_sik, start, mid, target)

    # 잘라서 나온 갯수가 n 이랑 같거나 크면?
    # 자른 길이는 적당하다.
    else:
        return binary_search(young_sik, mid, end, target)

print(binary_search(young_sik, start, end, n))