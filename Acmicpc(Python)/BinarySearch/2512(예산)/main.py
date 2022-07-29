import sys

input = sys.stdin.readline

n = int(input())

budgets = list(map(int, (input().split())))
max_money = int(input())

if max_money > sum(budgets):
    print(max(budgets))

print(max_money % n)

def binary_search(start, end, target, budgets):

    mid = (start + end) // 2


