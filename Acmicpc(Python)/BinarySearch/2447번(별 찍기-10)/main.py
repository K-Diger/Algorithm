import sys

input = sys.stdin.readline

n = int(input())
n = n ** 3

for i in range(n//3):
    print("*" * n)
    print()