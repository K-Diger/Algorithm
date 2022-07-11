import sys

input = sys.stdin.readline

n = int(input())

row = (2 * n) - 1

col_dp = [1, ]


for i in range(100):
    col_dp.append(col_dp[i] + 4)

col = col_dp[n-1]

print('*' * n + ' ' * (col - (2 * n)) + '*' * n)

for i in range(1, n-1):
    print(' ' * i + '*' + ' ' * (n - 2) + '*' + ' ' * (n + 2-(i * 2)), end="")
    print('*' + ' ' * (n - 2) + '*')

print(' ' * (n - 1) + '*' + ' ' * (n - 2) + '*' + ' ' * (n - 2) + '*')

for i in range(n-2, 0, -1):
    print(' ' * i + '*' + ' ' * (n-2) + '*' + ' ' * (n+2-(i*2)), end="")
    print('*' + ' ' * (n-2) + '*')


print('*' * n + ' ' * (col - (2 * n)) + '*' * n)