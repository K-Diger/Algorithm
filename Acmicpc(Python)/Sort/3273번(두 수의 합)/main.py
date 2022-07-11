# ai + aj = x (1 ≤ i < j ≤ n
# --> i 번째 수가 j 번째 수보다 작다.


# n 은 서로다른 양수의 갯수

# 셋째줄에 타겟넘버가 정해진다.

# n = 10만개까지 가능

# 정렬 후 분할정복을 해볼까

# 분할정복 메서드에 넘겨줘야할 타겟은?



import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.sort()
x = int(input())
count = int(0)


def divide_conquer(start, end, target):
    if start > end:
        return 0

    mid = (start + end) // 2

    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return divide_conquer(start, mid - 1, target)
    elif array[mid] < target:
        return divide_conquer(mid + 1, end, target)


# 리스트를 하나씩순회하면서, 그 원소값에 타겟하는 숫자를 빼서 매개변수로 넘겨준다.
# --> 타겟넘버 = 배열 내에서 현재 순회 중인 값 + 분할정복 내에서 현재 순회중인 값
# --> 분할정복 내에서 현재 순회중인 값 = 타겟넘버 - 배열 내에서 현재 순회중인 값

for item in array:
    count += divide_conquer(0, n - 1, x - item)

print(count // 2)
