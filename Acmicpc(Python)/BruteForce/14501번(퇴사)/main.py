import sys

input = sys.stdin.readline

n = int(input())

schedule = [list(map(int, input().split())) for i in range(n)]

calc_schedule = list([0] * n)

index = int(0)

while True:

    calc_schedule[i] = schedule[index][1]

    index = i + schedule[i][0]

    if index >= n:
        break
    print(index)

print(calc_schedule)