# import sys
#
# input = sys.stdin.readline
#
# document = input().strip()
# target = input().strip()
#
# start = int(0)
# last = len(target)
# count = int(0)
#
# while start < len(document):
#
#     # 입력 문자열의 일부가, 찾고자 하는 문자열에 일치하면
#     if document[start:last] == target:
#         count += 1
#         # 시작 인덱스 변경
#         start += last
#         # 끝 인덱스 변경
#         last += start
#     else:
#         start += 1
#         last += 1
#
# print(count)


import sys

input = sys.stdin.readline

document = input().strip()
target = input().strip()

start = int(0)
last = len(target)
count = int(0)

while start < len(document):

    # 입력 문자열의 일부가, 찾고자 하는 문자열에 일치하면
    if document[start:start+len(target)] == target:
        count += 1
        # 시작 인덱스 변경
        start += len(target)
    else:
        start += 1
print(count)
