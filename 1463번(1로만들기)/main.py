# 1. X가 3으로 나누어 떨어지면 3으로 나눈다
# 2. X가 2로 나누어 떨어지면 2로 나눈다.
# 3. 1을뺀다.

n = int(input())

dp = [0,0,1,1]

for i in range(4, n+1):
    dp.append(dp[i-1]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])

print(dp[n])























# import sys
#
# n = int(sys.stdin.readline())
# cnt = int(0)
#
# if n % 2 == 0: #짝수이면
#     n -= 1
#     cnt += 1
#
# while n != 1:
#     if n % 3 == 0:
#         n /= 3
#         cnt += 1
#     elif n % 2 == 0:
#         n /= 2
#         cnt += 1
#     else:
#         n -= 1
#         cnt += 1
#
# print(cnt)
















