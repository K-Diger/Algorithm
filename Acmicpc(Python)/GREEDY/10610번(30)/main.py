# 입력받은 숫자를 내림차순으로 정렬한다.

# 30으로 나눴을때 나머지가 0이면 30의 배수이니까

# 30의 배수이면 배열에 따로 넣고

# 그 배열의 max() 출력

import sys

input = sys.stdin.readline

n = list(input().strip())
n = sorted(n, reverse=True)

max_value = str()

for item in n:
    max_value += item

max_value = int(''.join(max_value))

if max_value % 30 == 0:
    print(max_value)
else:
    print(-1)

# for i in range(desc_value, 0, -1):
#     if desc_value % 30 == 0:
#         print(desc_value)
#         break
#     elif i < 30:
#         print(-1)
#         break