import sys

input = sys.stdin.readline


n, t = map(int, input().split())

bus_start, interval, bus_num = map(int, input().split())

bus_schedule = [bus_start]

for i in range(1, bus_num):
    bus_schedule.append(bus_schedule[i-1] + interval)

if bus_schedule[0] == t:
    print(0)

else:


def binary_search(start, end, target, bus_schedule):

    mid = (start + end) // 2

    if bus_schedule[mid] == target:
        print(0)
        return 0

    if start > end:
        return 0

