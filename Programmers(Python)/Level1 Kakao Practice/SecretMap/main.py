


# 결괏값 ["######","###  #","##  ##","#### ","#####","### # "]
# 기댓값 ["######","###  #","##  ##"," #### "," #####","### # "]


import re


def solution(n, arr1, arr2):

    or_operation = list()

    for i in range(n):
        or_operation.append(arr1[i] | arr2[i])

    for i in range(n):
        or_operation[i] = bin(or_operation[i])[2:n+2]

        if len(or_operation[i]) < n:
            or_operation[i] = ('0' * (n - len(or_operation[i]))) + or_operation[i]

    for i in range(n):
        or_operation[i] = re.sub('1', "#", or_operation[i])
        or_operation[i] = re.sub('0', " ", or_operation[i])

    return or_operation

# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]


n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

print(solution(n, arr1, arr2))