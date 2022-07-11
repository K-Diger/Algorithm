import sys

# a 가 가장 큰 값일 때
# b 에서 가장 작은 값이랑 매핑 되도록하면 될 것 같다.

# --> a 내림차순
# --> b 오름차순

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = int(0)

a.sort(reverse=True)
b.sort()

for i in range(n):
    result += a[i] * b[i]
print(result)