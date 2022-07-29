import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

dp = [[]] * n

for i in range(n-1):
    current = a[i]
    for j in range(i, n):
        if current < a[j]:
            current = a[j]
            dp[i].append(a[j])