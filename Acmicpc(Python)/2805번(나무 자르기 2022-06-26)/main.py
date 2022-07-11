import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tree_length = list(map(int, input().split()))

start = 1
end = max(tree_length)

def binary_search(tree_length, start, end, target):
    # n = 1
    # m = 1000000000
    # tree_length = 1000000000
    # 나무는 하나있고, 1000000000 의 길이의 나무를 가져가고싶은데, 1000000000의 길이의 나무가 하나 있는거면
    # 그냥 그 나무를 통째로 가져가야댐, 짜를 필요가 없음
    if end == target:
        return 0

    # mid 의 길이는, start 와 나무 길이의 최댓값의 중간값
    # mid 의 길이로 짜를때
    mid = (start + end) // 2

    # 몇 개가 나오는가?
    count = 0

    # 탐색할 경우가 2개만 남았다 --> 끝
    if start == end - 1:
        return start

    # 첫 순회 mid = (1 + 20) // 2 == 10
    for item in tree_length:
        if item - mid < 0:
            count += 0
        else:
            count += (item - mid)

    # 잘라서 나온 길이의 합이 target 보다 작으면?
    # 자르는 값인, mid 값이 너무 큰거다.
    # 즉 중간 분기점에서 오른쪽으로 더 살필 필요가 없다.
    if count < target:
        return binary_search(tree_length, start, mid, target)

    # 잘라서 나온 길이가 n 이랑 같거나 크면?
    # 자른 길이는 적당하다.
    else:
        return binary_search(tree_length, mid, end, target)

print(binary_search(tree_length, start, end, m))