import sys

input = sys.stdin.readline

t = int(input())

zero, one = int(0), int(0)

zero_dp = [0] * 41
one_dp = [0] * 41

zero_dp[0] = 1
one_dp[0] = 0

zero_dp[1] = 0
one_dp[1] = 1

for i in range(2, 41):
    zero_dp[i] = zero_dp[i - 1] + zero_dp[i - 2]
    one_dp[i] = one_dp[i - 1] + one_dp[i - 2]

for j in range(t):
    tc = int(input())
    print(zero_dp[tc], one_dp[tc])