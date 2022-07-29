import sys

input = sys.stdin.readline

n = int(input())
sang_geun_deck = sorted(list(map(int, input().split())))

m = int(input())
target_deck = list(map(int, input().split()))


def binary_search(start, end, sang_geun_deck, target):
    mid = (start + end) // 2

    if start > end:
        print("0", end=" ")
        return

    if sang_geun_deck[mid] == target:
        print("1", end=" ")
        return

    elif sang_geun_deck[mid] > target:
        end = mid - 1

    elif sang_geun_deck[mid] < target:
        start = mid + 1

    binary_search(start, end, sang_geun_deck, target)


for i in range(m):
    # print(binary_search(0, len(sang_geun_deck) - 1, sang_geun_deck, target_deck[i]), end=" ")
    binary_search(0, len(sang_geun_deck)-1, sang_geun_deck, target_deck[i])
