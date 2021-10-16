
n = int(input())

deck_nums = list(map(int, input().split()))

m = int(input())

target_nums = list(map(int, input().split()))

cnt = [int(0)] * m


cnt = deck_nums.count(target_nums)

print(cnt)