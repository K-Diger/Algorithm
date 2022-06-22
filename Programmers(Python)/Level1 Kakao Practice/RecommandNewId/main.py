''''
3 ~ 15 자
a-z, -, _, .
. 는 처음과 끝에 사용 불가, 연속으로 사용 불가


1단계: 대 -> 소
2단계 -> 문자 필터링
3단계 -> . 2개이상 -> .개로
4단계 -> . 처음이나 끝에 있으면 제거
5단계 -> 빈 문자열이면 a
6단계 -> 16자 이상 시 -> 처음 15자까지
7단계 -> 2자 이하면, 마지막 문자를 3이 될때 까지 반복
'''

import re

def solution(new_id):

    # Step 1 : 대문자를 소문자로 치환하기
    new_id = new_id.lower()

    # Step 2 : 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    new_id = re.sub('[^a-z0-9-_.]', "", new_id)

    # Step 3 : 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id = re.sub('\.\.+', ".", new_id)

    # Step 4 : 마침표(.)가 처음이나 끝에 위치한다면 제거
    new_id = re.sub('^(\.)', "", new_id)
    new_id = re.sub('(\.$)', "", new_id)

    # Step 5 : 빈 문자열이라면, new_id에 "a"를 대입
    if new_id == '':
        new_id = 'a'

    # Step 6 :
    # 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거,
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.

    if len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub('(\.$)', "", new_id)

    # Step 7 : 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝으로

    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[len(new_id)-1]

    return new_id


# solution("...!@BaT#*..y.abcdefghijklm")
solution("=.=")