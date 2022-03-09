# 시나리오
# n개 원판이 있으면 n-1개까지는 다른 막대기로 몰빵
# 마지막 한개는 나머지 막대기로
# 위 과정 계속 반복하기 n-1 n-2 n-3 ... 1

#start = 첫번째 막대기
#destination = 두번째 막대기
#another = 세번째 막대기

import sys

input = sys.stdin.readline

circleInput = int(input().split()) #원판갯수 입력받기
countMoving = int(0) #카운터

#원판 갯수가 홀수일때는 another로
#원판 갯수가 짝수일때는 destination로 보내야함

#memo: 첫번째에서 세번째로 옮기는게 목적이면 모든 이동 과정의 기본은 start -> another
#매개변수에서 start 위치가, 움직일 대상이 되는것, destination위치가 이동할 위치를 가리키는 것이 된다.
def hanoiTop(circle, start, destination, another):
    global countMoving
    if circle == 1:
        print(start, another)
        countMoving += 1
    else:
        hanoiTop(circle-1, start, another, destination)
        countMoving += 1
        print(start, another)
        hanoiTop(circle-1, destination, start, another)

    return countMoving


# 1일때 1
# 2일때 3
# 3일때 7
# 4일때 15
# 5일때 31
# 6일때 63
#이동횟수는 2^n-1

print((2**circleInput)-1)
hanoiTop(circleInput, 1, 2, 3)