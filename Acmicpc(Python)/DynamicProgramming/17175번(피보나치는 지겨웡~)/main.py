import sys

input = sys.stdin.readline

n = int(input())

def dynamic_programming(n):
    dp = [0] * 51

    dp[0] = 1
    dp[1] = 1

    if n == 0:
        return dp[n]
    elif n == 1:
        return dp[n]

    for i in range(2, 51):
        dp[i] = dp[i - 1] + dp[i - 2] + 1

    return dp[n] % 1000000007


print(dynamic_programming(n))
