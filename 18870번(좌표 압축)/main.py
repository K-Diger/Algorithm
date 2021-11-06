'''
입력받은 배열에서 압축하려는 수보다 작은 수의 갯수를 찾아 출력하는것

배열에서 압축하는 수보다 작은 것을 count 배열에 넣기

3을 압축 - > 1 2
'''

import sys

input = sys.stdin.readline

n = int(input())

x = list(map(int, input().split()))

new_x = []

for overlap in x: # 중복제거를 위한 반복
    if overlap not in new_x:
        new_x.append(overlap)

new_x.sort()

cnt = []

i = int(0)
j = int(0)

while True:
    if new_x[j] == x[i]:
        cnt.append(j)
        i += 1
    j += 1

    if j == len(new_x):
        j = 0
    if i == n:
        break

print(cnt)

# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# x = list(map(int, input().split()))
#
# new_x = []
#
# '''
# 1 2 3 4 5 6 7
#
# 압축하는 수보다 작은 수의 갯수를 찾아 출력하는것
#
# 배열에서 압축하는 수보다 작은 것을 count 배열에 넣기
#
# 3을 압축 - > 1 2
# '''
#
# for overlap in x:
#     if overlap not in new_x:
#         new_x.append(overlap)
#
# new_x.sort()
#
# cnt = []
#
# for i in range(n):
#     for j in range(len(new_x)):
#         if new_x[j] == x[i]:
#             cnt.append(j)
#
# print(cnt)