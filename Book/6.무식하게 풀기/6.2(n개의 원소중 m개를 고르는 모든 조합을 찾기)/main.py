# 하나의 리스트에서 모든 조합을 계산해야할 때, permutations, combinations
# 두개의 리스트에서 모든 조합을 계산해야할 때, product


from itertools import permutations
from itertools import combinations
from itertools import product




n = int(input())
m = int(input())

## 순열이기 때문에 순서를 바꿨을 때 똑같은 조합이면 포함시키지 않음
result_permutations = list(permutations(range(n), m))

## 조합이기 대문에 순서를 바꿨을 때 도 똑같은 조합을 포함시킴
result_combinations = list(combinations(range(n), m))

print(result_permutations)
print(result_combinations)