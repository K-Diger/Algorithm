import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

numbers = list(i for i in range(2, n + 1))
prime_numbers = deque()


for i in range(2, len(numbers) + 1):
    for j in range(2, int((i ** 0.5) + 1)):
        if i % j == 0:
            break
    else:
        prime_numbers.append(i)


for i in prime_numbers:
    if m <= i <= n:
        print(i)

# 소수는 1, 자기자신만을 약수로 가진다.
# 해당 수의 제곱근 까지만 확인한다. (약수는 대칭이므로, 절반까지만 봐도 되기 때문)