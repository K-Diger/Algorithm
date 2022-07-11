import sys

input = sys.stdin.readline

'''

5
0 4
1 2
1 -1
2 2
3 3

1 -1
1 2
2 2
3 3
0 4

'''

# 다른 문제들을 풀다가 2차원 배열을 람다로 정렬하는 꼴을 봤었다.

# sort 함수에, lambda를 key로 가지고, x[1] 은 col, x[0] 은 row 느낌이었던거같다.

# 해보자

n = int(input())

coordinate = [list(map(int, input().split())) for i in range(n)]

coordinate.sort(key=lambda x: (x[1], x[0]))

for item in coordinate:
    print(item[0], item[1])