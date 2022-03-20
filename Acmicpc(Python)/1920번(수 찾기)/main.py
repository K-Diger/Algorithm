import sys

input = sys.stdin.readline

n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

res = []

for i in range(n):
    if m_arr[i] in n_arr:
        res.append(1)
    else:
        res.append(0)

for i in range(len(res)):
    print(res[i])