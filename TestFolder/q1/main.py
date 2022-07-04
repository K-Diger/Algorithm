# 글자 사이 가로 + 세로 거리를 계산하고,

# 거리의 총합과 글자와 글자 사이를 계산한 거리 개수를 리턴

# 거리 += (x1 - x2) + (y1 - y2)
# 현재좌표 수정 = (x1 + x2) + (y1 + y2)

keyboard = ["가", "호", "저", "론", "남", "드", "부", "이", "프", "설"], ["알", "크", "청", "올", "키", "초", "트", "을", "배", "주"], ["개",
                                                                                                                    "캠",
                                                                                                                    "산",
                                                                                                                    "대",
                                                                                                                    "단",
                                                                                                                    "지",
                                                                                                                    "역",
                                                                                                                    "구",
                                                                                                                    "너",
                                                                                                                    "양"], [
               "라", "로", "권", "교", "마", "쿼", "파", "송", "차", "타"], ["코", "불", "레", "뉴", " ", "서", "한", "산", "리", "개"], [
               "터", "강", "봄", "토", "캠", "상", "호", "론", "운", "삼"], ["보", "람", "이", "경", "아", "두", "프", "바", "트", "정"], [
               "스", "웨", "어", "쿼", "일", "소", "라", "가", "나", "도"], ["판", "자", "비", "우", "사", "거", "왕", "태", "요", "품"], [
               "안", "베", "차", "캐", "민", "광", "재", "봇", "북", "하"]

word = "불레뉴캠프"


def solution(word, keyboard):

    # answer[0] = 거리값
    # answer[1] = 카운팅
    answer = [0, -1]

    current_x, x2, current_y, y2 = int(), int(), int(), int()

    current_distance = [[]]

    # 문자가 단어장에 있을때 -> 거리계산
    for i in range(len(word)):
        item = word[i]

        if item * len(word) == word:
            answer[0] = 0
            answer[1] = 1
            break

        # x좌표 하나씩 순회
        for x in range(len(keyboard)):
            # y 좌표 하나씩 순회
            for y in range(len(keyboard)):

                # 해당 좌표에서, 현재 타겟인 item이 있으면
                # 좌표 저장
                if item in keyboard[x][y]:
                    current_distance = [x, y]

                    answer[0] += current_distance[0] - current_distance[y]

                    print(current_distance)
        answer[1] += 1


    return answer


print(solution(word, keyboard))
