def solution(phone_number):
    answer = list(phone_number)
    cnt = len(answer[:-4])  # 뒷번호 4자리를 제외한 전화번호 문자 갯수

    answer[:-4] = "*" * cnt  # cnt갯수만큼 나머지 문자열 *로 변환. 방향 : <--

    phone_number = "".join(answer)  # 리턴해줄 변수를 문자열로 변환하기

    return phone_number