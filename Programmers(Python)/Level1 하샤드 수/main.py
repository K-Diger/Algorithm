x = 18


# 자리수의 합으로 나눠떨어지는가?
def solution(x):
    num = 0
    x = str(x)  # 입력 정수 문자열화
    for i in range(len(x)):  # 문자열 길이 만큼 반복(수의 길이만큼 반복)
        num += int(x[i])  # (각 자리수를 num 변수에 합하며 넣어주기)

    if (int(x) % int(num)) == 0:
        return True
    return False
