import sys

n = int(sys.stdin.readline()) #n은 홀수
numbers = [int(sys.stdin.readline()) for i in range(n)]

#평균
print(round(sum(numbers)/n))

#중앙값
center_value_idx = int(n/2)
center_value = sorted(numbers)
print(center_value[center_value_idx])

#최빈값 여러개 있을 경우에는, 두번째로 작은 값 출력
numbers.sort()
from collections import Counter

if n == 1:
    print(numbers[0])
else:
    mode_value = Counter(numbers).most_common()
    if n > 1:
        if mode_value[0][1] == mode_value[1][1]:
            print(mode_value[1][0])
        else:
            print(mode_value[0][0])

#범위
print(max(numbers) - min(numbers))