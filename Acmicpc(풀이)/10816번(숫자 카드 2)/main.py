n = int(input()) # 상근이가 가지고 있는 카드 갯수
deck_nums = list(map(int, input().split())) # 상근이가 가지고 있는 카드에 적힌 수

m = int(input()) # 타겟 카드 갯수를 정하기
target_nums = list(map(int, input().split())) # 이 타겟 수에 대해서 상근이가 몇개를 가지고 있을까?


cnt = [int(0)] * 500000

for i in range(n):
    cnt[deck_nums[i]] += 1

for j in range(len(target_nums)):
    print(deck_nums.count(target_nums[j]), end=" ")