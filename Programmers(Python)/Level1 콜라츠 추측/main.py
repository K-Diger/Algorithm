num = int(6)

def solution(num):
    if num == 1: #입력숫자가 1인지 먼저 체크
        return 0

    cnt = int(0)
    while cnt < 500:

        if num % 2 == 0: #짝수일때
            num //= 2
            cnt += 1
            if num == 1:
                return cnt
        else: #홀수일때
            num = (num*3) + 1
            cnt += 1
            if num == 1:
                return cnt
    cnt = -1
    return cnt

print(solution(num))