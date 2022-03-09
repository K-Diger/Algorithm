# import sys
#
# n = int(sys.stdin.readline())
# arr = []
# sum =[]
# # 두 수의 합을 구하고 그 합이 작은 순으로 출력
# # 만약 합이 같다면 그 숫자중에 X가 더 작은 값을 기준으로 출력 -> Y가
#
# for i in range(n):
#     arr.append(list(map(int, sys.stdin.readline().split())))
#
# for i in range(n):
#     sum.append(arr[i])
#
# arr.sort() # 두 수의 입력을 담은 배열을 정렬
# sum.sort() # 두 수의 합을 오름차순으로 정렬
#
# for i in range(n-1):
#     if sum[i] == sum[i+1]: # 두수의 합이 같고
#         if int(arr[i][0]) > int(arr[i+1][0]): # X좌표를 비교해서, X좌표가 더 크다면
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#
# for i in range(n):
#     print(int(arr[i][0]), int(arr[i][0]))

import sys
n = int(sys.stdin.readline())

arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
arr.sort(key=lambda x:(x[0], x[1]))

for i in range(n):
    print(arr[i][0], arr[i][1])