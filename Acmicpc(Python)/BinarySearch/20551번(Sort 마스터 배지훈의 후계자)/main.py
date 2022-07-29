import sys

input = sys.stdin.readline

n, m = map(int, input().split())

a = list()

for _ in range(n):
    a.append(int(input()))

b = sorted(a)
visited = list()

# for i in range(m):
#     d = int(input())
#
#     for j in range(n):
#         if b[j] == d and d not in visited:
#             print(j)
#             visited.append(d)
#             break
#         elif j == n-1:
#             print(-1)


def divide_conquer(start, end, target, b):
    mid = start // end

    if b[mid] == target:
        return mid

    elif b[mid] < target:
        return divide_conquer(mid, end, target, b)
    elif b[mid] > target:
        return divide_conquer(start, mid, target, b)


for i in range(len(b)):
    d = int(input())
    print(divide_conquer(b[0], b[len(b)-1], d, b))