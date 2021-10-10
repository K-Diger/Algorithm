serial = list(map(int, input().split()))
res = int()
for i in range(5):
    res += serial[i] ** 2

print(res%10)