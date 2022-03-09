import sys
from collections import deque

n = int(sys.stdin.readline())

'''
12345
    2345
        3452
            452
                524
                    24
                        42
                            2

'''
cards = deque()
for i in range(1, n+1):
    cards.append(i)

while len(cards) != 1: # deque 길이가 1일때 까지
    cards.popleft() #맨 왼쪽 원소 삭제
    temp = cards.popleft() # 그 다음 맨 왼쪽원소를 temp에 저장
    cards.append(temp) # temp에 저장한 원소값을 맨 뒤로 다시 추가

print(cards[0])